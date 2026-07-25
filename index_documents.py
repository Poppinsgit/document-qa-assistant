from pypdf import PdfReader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_core.documents import Document
from langchain_chroma import Chroma

from embeddings import MyEmbeddings


def create_vector_db(pdf_path):

    reader = PdfReader(pdf_path)

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=50
    )

    all_documents = []

    for page_number, page in enumerate(reader.pages):

        page_text = page.extract_text()

        if not page_text:
            continue

        chunks = splitter.split_text(page_text)

        for i, chunk in enumerate(chunks):
            all_documents.append(
                Document(
                    page_content=chunk,
                    metadata={
                        "source": pdf_path,
                        "page": page_number + 1,
                        "chunk_id": i
                    }
                )
            )

    embedding_function = MyEmbeddings()

    Chroma.from_documents(
        documents=all_documents,
        embedding=embedding_function,
        persist_directory="vector_db"
    )

    print("✅ Vector DB created!")
    if __name__ == "__main__":
        create_vector_db("documents/UAE_labour_law.pdf")