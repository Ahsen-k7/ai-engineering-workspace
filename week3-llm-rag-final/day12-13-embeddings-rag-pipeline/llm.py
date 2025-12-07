# football_assistant.py
import os
import shutil
from dotenv import load_dotenv
from langchain_chroma import Chroma
from langchain_google_genai import ChatGoogleGenerativeAI, GoogleGenerativeAIEmbeddings
from langchain_google_genai._common import GoogleGenerativeAIError
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough
from langchain_core.prompts import ChatPromptTemplate
from langchain_community.document_loaders import PyPDFLoader, TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from google.api_core.exceptions import ResourceExhausted

load_dotenv()

# ================== CONFIG ==================
CHROMA_PATH = "./football_chromadb"
COLLECTION_NAME = "premier_league_knowledge"

# Use Gemini for both embeddings and chat
embeddings = GoogleGenerativeAIEmbeddings(
    model="models/embedding-001",
    google_api_key=os.getenv("GEMINI_API_KEY")
)

llm = ChatGoogleGenerativeAI(
    model="gemini-1.5-flash-001",
    google_api_key=os.getenv("GEMINI_API_KEY"),
    temperature=0.7,
    convert_system_message_to_human=True
)

# ================== LOAD & SPLIT DOCUMENTS ==================
def load_football_documents():
    docs = []
    
    # Add your football PDFs or text files here
    football_files = [
        "Football.pdf"
    ]
    
    for file_path in football_files:
        if file_path.endswith(".pdf"):
            loader = PyPDFLoader(file_path)
        else:
            loader = TextLoader(file_path, encoding="utf-8")
        docs.extend(loader.load())
    
    # Better splitter for clean chunks
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=200,
        length_function=len
    )
    return text_splitter.split_documents(docs)

# ================== BUILD OR LOAD VECTOR STORE ==================
def get_retriever():
    if os.path.exists(CHROMA_PATH):
        print("Loading existing Chroma database...")
        vectorstore = Chroma(
            persist_directory=CHROMA_PATH,
            embedding_function=embeddings,
            collection_name=COLLECTION_NAME
        )
    else:
        print("Creating new Chroma database...")
        documents = load_football_documents()
        vectorstore = Chroma.from_documents(
            documents=documents,
            embedding=embeddings,
            persist_directory=CHROMA_PATH,
            collection_name=COLLECTION_NAME
        )
        print(f"Added {len(documents)} chunks to Chroma")
    
    return vectorstore.as_retriever(search_kwargs={"k": 5})

# ================== FORMAT DOCS ==================
def format_docs(docs):
    # flatten retrieved document contents with blank line separators
    return "\n\n".join(doc.page_content for doc in docs)

# ================== PROMPT — FOOTBALL EXPERT ==================
prompt = ChatPromptTemplate.from_template("""
You are **FootballGuru**, the world's most passionate and accurate football assistant.
You live and breathe football. You know every stat, rule, history, and drama.

Use only answer football-related questions.
If the question is not about football, reply: "Bro, I'm a football expert only! Ask me about Messi, Premier League, tactics, transfers, anything football!"

Context from football knowledge base:
{context}

Question: {question}

Answer like a true football fan — energetic, accurate, and fun!
""")

# ================== RAG CHAIN ==================
retriever = get_retriever()

rag_chain = (
    {"context": retriever | format_docs, "question": RunnablePassthrough()}
    | prompt
    | llm
    | StrOutputParser()
)

# ================== TEST IT ==================
if __name__ == "__main__":
    print("Football Assistant Ready!\n")
    
    while True:
        question = input("\nAsk me anything about football (or 'quit' to exit): ")
        if question.lower() in ["quit", "exit", "bye"]:
            print("Keep loving football! Peace")
            break
        
        print("\nThinking...")
        try:
            response = rag_chain.invoke(question)
            print(f"\nFootballGuru: {response}")
        except (GoogleGenerativeAIError, ResourceExhausted) as e:
            error_msg = str(e)
            if "quota" in error_msg.lower() or "429" in error_msg:
                print("\n⚠️  API Quota Exceeded!")
                print("You've exceeded your Google Gemini API quota.")
                print("Please check your plan and billing details at:")
                print("https://ai.google.dev/gemini-api/docs/rate-limits")
                print("\nYou may need to:")
                print("  - Wait for the quota to reset (daily limits reset at midnight)")
                print("  - Check your Google Cloud Console billing and quotas")
                print("  - Consider upgrading your plan if you need higher limits")
            else:
                print(f"\n❌ Error: {error_msg}")
        except Exception as e:
            print(f"\n❌ An unexpected error occurred: {str(e)}")
        
        print("\n" + "─" * 80)