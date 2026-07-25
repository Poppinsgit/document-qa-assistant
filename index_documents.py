from pypdf import PdfReader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_core.documents import Document
from langchain_chroma import Chroma

from embeddings import MyEmbeddings


# 1. Read PDF
pdf_path = "documents/UAE_labour_law.pdf"

reader = PdfReader(pdf_path)

text = ""

for page in reader.pages:
    page_text = page.extract_text()
    if page_text:
        text += page_text


print("Characters:", len(text))


# 2. Split text into chunks
splitter = RecursiveCharacterTextSplitter(
    chunk_size=500,
    chunk_overlap=50
)

chunks = splitter.split_text(text)

print("Total chunks:", len(chunks))


# 3. Convert chunks into LangChain Documents
documents = []

for i, chunk in enumerate(chunks):
    documents.append(
        Document(
            page_content=chunk,
            metadata={"chunk_id": i}
        )
    )

print("Documents created:", len(documents))


# 4. Load embedding model
embedding_function = MyEmbeddings()


# 5. Store in Chroma
vector_db = Chroma.from_documents(
    documents=documents,
    embedding=embedding_function,
    persist_directory="vector_db"
)


print("✅ Vector database created!")