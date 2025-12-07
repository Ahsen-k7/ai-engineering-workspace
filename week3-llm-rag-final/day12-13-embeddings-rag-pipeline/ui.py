import gradio as gr
from llm2 import chain
from langchain_google_genai._common import GoogleGenerativeAIError
from google.api_core.exceptions import ResourceExhausted

def chat(question, history):
    if question == "":
        return "Please ask a question"
    
    try:
        return chain.invoke(question)
    except (GoogleGenerativeAIError, ResourceExhausted) as e:
        error_msg = str(e)
        if "quota" in error_msg.lower() or "429" in error_msg:
            return "⚠️ API Quota Exceeded: You've exceeded your Google Gemini API quota. Please check your plan and billing details at https://ai.google.dev/gemini-api/docs/rate-limits. You may need to wait for the quota to reset or upgrade your plan."
        else:
            return f"❌ Error: {error_msg}"
    except Exception as e:
        return f"❌ An unexpected error occurred: {str(e)}"
    
gr.ChatInterface(
    fn=chat
).launch()
