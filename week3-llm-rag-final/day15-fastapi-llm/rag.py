# rag.py
import os
from dotenv import load_dotenv

from qdrant_client import QdrantClient
from qdrant_client.models import Distance, VectorParams

from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_groq import ChatGroq

from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

HF_TOKEN = os.getenv("HF_TOKEN")
GROQ_API_KEY = os.getenv("GROQ_API_KEY")


class FootballRAG:
    def __init__(self):
        # Embeddings
        self.embeddings = HuggingFaceEmbeddings(
            model_name="sentence-transformers/all-MiniLM-L6-v2"
        )

        # Qdrant vector DB
        self.qdrant = QdrantClient(path="./qdrant_db")

        # Groq LLM with token tracking
        self.llm = ChatGroq(
            model="llama-3.1-8b-instant",
            temperature=0.3,
        )

        # Prompt
        self.prompt = ChatPromptTemplate.from_template("""
        You are a Football Assistant AI. 
        Only answer using the context below. 
        If information is not found, say you don't know.

        CONTEXT:
        {context}

        QUESTION:
        {question}

        Answer:
        """)

    # ----------------------------
    # RETRIEVE K CHUNKS
    # ----------------------------
    def retrieve(self, query, k=5):
        q_emb = self.embeddings.embed_query(query)

        results = self.qdrant.search(
            collection_name="football_collection",
            query_vector=q_emb,
            limit=k,
        )

        return [r.payload["text"] for r in results]

    # ----------------------------
    # MAIN RAG ANSWER
    # ----------------------------
    def answer(self, query):
        sources = self.retrieve(query)
        context = "\n\n".join(sources)

        chain = (
            {"context": lambda _: context, "question": lambda _: query}
            | self.prompt
            | self.llm
            | StrOutputParser()
        )

        output = chain.invoke(query)

        # token counts
        usage = self.llm.get_num_tokens(context + query)

        return {
            "answer": output,
            "sources": sources,
            "token_usage": usage
        }


rag = FootballRAG()
