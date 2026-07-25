import os

from langchain_google_genai import ChatGoogleGenerativeAI


llm = ChatGoogleGenerativeAI(
    model="gemini-3-flash-preview",
    google_api_key=os.getenv(
        "GOOGLE_API_KEY"
    ),
    temperature=0.2
)



def ask_llm(question, context):

    prompt = f"""

You are a document assistant.

Answer only using the context provided.

If the answer is not present,
say:
"I could not find this information in the document."

Context:

{context}


Question:

{question}


Answer:

"""


    response = llm.invoke(prompt)

    return response.content