import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

# Gemini Pro (free tier works perfectly)
llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    google_api_key=os.getenv("GEMINI_API_KEY"),
    temperature=0.3
)

# Prompt engineering — this is the real skill
template = """
You are an expert AI engineering mentor. Answer clearly and concisely.

Context: The student is doing a 1-month AI engineering internship.
Question: {question}

Answer in maximum 3 sentences.
"""

prompt = ChatPromptTemplate.from_template(template)
chain = prompt | llm | StrOutputParser()

# Test questions
questions = [
    "What is the capital of France?",
    "Explain RAG in simple terms",
    "Why do we use vector databases?"
]

for q in questions:
    print(f"\nQ: {q}")
    print(f"A: {chain.invoke({'question': q})}")
    print("-" * 50)