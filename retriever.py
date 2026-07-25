from langchain_chroma import Chroma
from embeddings import MyEmbeddings


def get_relevant_chunks(question):

    embedding_function = MyEmbeddings()

    vector_db = Chroma(
        persist_directory="vector_db",
        embedding_function=embedding_function
    )

    results = vector_db.similarity_search(
        question,
        k=3
    )

    context = "\n\n".join(
        [doc.page_content for doc in results]
    )

    return context, results