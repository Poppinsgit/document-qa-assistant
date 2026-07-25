from pypdf import PdfReader
from langchain_text_splitters import RecursiveCharacterTextSplitter


pdf_path = "documents/sample.pdf"

reader = PdfReader(pdf_path)

text = ""

for page in reader.pages:
    text += page.extract_text()


splitter = RecursiveCharacterTextSplitter(
    chunk_size=500,
    chunk_overlap=50
)


chunks = splitter.split_text(text)


print("Total chunks:", len(chunks))

print("\nFirst chunk:")
print(chunks[0])