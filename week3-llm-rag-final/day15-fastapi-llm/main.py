# main.py
from fastapi import FastAPI
from pydantic import BaseModel
from rag import rag

app = FastAPI(title="Football RAG API")

class Query(BaseModel):
    question: str

@app.post("/qa")
def qa_endpoint(query: Query):
    """
    RAG endpoint:
    - takes a question
    - retrieves docs
    - calls Groq LLM
    - returns answer + sources + token usage
    """
    response = rag.answer(query.question)
    return {
        "question": query.question,
        "answer": response["answer"],
        "sources": response["sources"],
        "token_usage": response["token_usage"],
    }
