import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv()

llm = ChatGoogleGenerativeAI(
    model="gemini-2.0-flash",
    temperature=0.2,
    google_api_key=os.getenv("GOOGLE_API_KEY")
)


def ask_llm(question, context):
    prompt = f"""
You are a helpful AI assistant.

Answer ONLY using the context below.
If the answer is not present, say:
"I could not find this information in the document."

Context:
{context}

Question:
{question}
"""

    try:
        response = llm.invoke(prompt)
        return response.content
    except Exception as e:
        return f"❌ Gemini Error:\n{e}"