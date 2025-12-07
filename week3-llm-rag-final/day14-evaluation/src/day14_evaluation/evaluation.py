# src/evaluate.py
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
import json
import os

load_dotenv()

llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash-001", temperature=0.3)

# OFFICIAL DAY 14: PromptTemplate mastery
template = ChatPromptTemplate.from_messages([
    ("system", "You are a football expert with perfect recall. Answer in 1-2 sentences only."),
    ("human", "{question}")
])

chain = template | llm | StrOutputParser()

# Ground truth dataset (the real evaluation harness)
qa_pairs = [
    {
        "question": "Who has won more Ballon d'Or awards?",
        "ground_truth": "Lionel Messi has won 8 Ballon d'Or awards, more than any other player."
    },
    {
        "question": "How many World Cups has Brazil won?",
        "ground_truth": "Brazil has won the World Cup 5 times (1958, 1962, 1970, 1994, 2002)."
    },
    {
        "question": "What is the offside rule in simple terms?",
        "ground_truth": "A player is offside if they are nearer to the opponent's goal line than both the ball and the second-last opponent when the ball is played to them."
    },
    {
        "question": "Which club has won the most English league titles?",
        "ground_truth": "Manchester United have won 20 English league titles."
    }
]

print("DAY 14 — EVALUATION HARNESS RUNNING\n")
print("="*70)

results = []

for i, pair in enumerate(qa_pairs, 1):
    answer = chain.invoke({"question": pair["question"]})
    
    print(f"Q{i}: {pair['question']}")
    print(f"Answer: {answer}")
    print(f"Truth: {pair['ground_truth']}")
    print(f"Match: {'YES' if answer.strip().lower() in pair['ground_truth'].lower() or pair['ground_truth'].lower() in answer.strip().lower() else 'NO'}")
    print("-" * 70)
    
    results.append({
        "question": pair["question"],
        "generated": answer,
        "ground_truth": pair["ground_truth"],
        "match": "YES" in answer or pair["ground_truth"] in answer
    })

# Final score
correct = sum(1 for r in results if r["match"])
print(f"\nFINAL SCORE: {correct}/{len(qa_pairs)} correct answers")
print(f"Accuracy: {correct/len(qa_pairs)*100:.1f}%")

# Save results
with open("evaluation_results.json", "w") as f:
    json.dump(results, f, indent=2)

print("\nResults saved to evaluation_results.json")
print("DAY 14 OFFICIALLY COMPLETE — PromptTemplate + Evaluation Harness")