# RAG USING GROK (GROQ) + HUGGINGFACE EMBEDDINGS
import os
from dotenv import load_dotenv

from langchain_chroma import Chroma
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough
from langchain_core.prompts import ChatPromptTemplate
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import CharacterTextSplitter

# HuggingFace Embeddings
from sentence_transformers import SentenceTransformer

# Grok
from langchain_groq import ChatGroq


# ----------------------------------------------------------------
# 📌 Load environment
# ----------------------------------------------------------------
load_dotenv()
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

if not GROQ_API_KEY:
    raise ValueError("❌ Missing GROQ_API_KEY in .env")


# ----------------------------------------------------------------
# 📌 1. Load PDFs
# ----------------------------------------------------------------
loader = PyPDFLoader("Football.pdf")
documents = loader.load()


# ----------------------------------------------------------------
# 📌 2. Chunk PDF
# ----------------------------------------------------------------
splitter = CharacterTextSplitter(
    separator="\n",
    chunk_size=800,
    chunk_overlap=100
)

docs = splitter.split_documents(documents)


# ----------------------------------------------------------------
# 📌 3. Free HuggingFace Embeddings
# ----------------------------------------------------------------
hf_model = SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2")

class HFEmbeddingWrapper:
    """Wrap HuggingFace model to make it compatible with Chroma."""
    def embed_documents(self, texts):
        return hf_model.encode(texts).tolist()

    def embed_query(self, text):
        return hf_model.encode(text).tolist()


embeddings = HFEmbeddingWrapper()


# ----------------------------------------------------------------
# 📌 4. Create / Load Chroma Vector DB
# ----------------------------------------------------------------
def load_chunks(docs):
    vectorstore = Chroma(
        persist_directory="./chromadb",
        embedding_function=embeddings,
        collection_name="football_collection",
    )
    print("Adding docs to Chroma...")
    vectorstore.add_documents(docs)
    print("Done!")


# Run once to create db
# load_chunks(docs)


def get_retriever():
    vectorstore = Chroma(
        persist_directory="./chromadb",
        embedding_function=embeddings,
        collection_name="football_collection",
    )
    return vectorstore.as_retriever(search_kwargs={"k": 4})


retriever = get_retriever()


# ----------------------------------------------------------------
# 📌 5. Grok LLM (xAI) for text generation
# ----------------------------------------------------------------
LLM = ChatGroq(
    api_key=GROQ_API_KEY,
    model="llama-3.1-8b-instant",
    temperature=0.1,
)


# ----------------------------------------------------------------
# 📌 6. Football RAG Prompt
# ----------------------------------------------------------------
prompt = ChatPromptTemplate.from_template("""
You are a **Football Assistant AI**.
Use ONLY the context to answer.
If unknown, say: "I don't have enough information."

CONTEXT:
{context}

QUESTION:
{question}

ANSWER:
""")


def format_docs(docs):
    return "\n\n".join(doc.page_content for doc in docs)


# ----------------------------------------------------------------
# 📌 7. Build the RAG pipeline
# ----------------------------------------------------------------
chain = (
    {"context": retriever | format_docs, "question": RunnablePassthrough()}
    | prompt
    | LLM
    | StrOutputParser()
)

# Example:
print(chain.invoke("What is the offside rule?"))
