from langchain_chroma import Chroma
from embeddings import MyEmbeddings
from llm import ask_llm


# Load embedding function
embedding_function = MyEmbeddings()


# Load existing Chroma database
vector_db = Chroma(
    persist_directory="vector_db",
    embedding_function=embedding_function
)


# User question
question = input("Ask your question: ")


# Retrieve relevant chunks
results = vector_db.similarity_search(
    question,
    k=3
)


# Combine retrieved chunks
context = ""

for result in results:
    context += result.page_content + "\n\n"


# Send context + question to LLM
answer = ask_llm(
    context=context,
    question=question
)


print("\n========== AI Answer ==========\n")
print(answer)