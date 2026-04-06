from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from config import chunkSize, chunkOverlap

def loadSplit(pdfPath : str):
    loader = PyPDFLoader(pdfPath)
    documents = loader.load()

    splitter = RecursiveCharacterTextSplitter(
        chunk_size = chunkSize,
        chunk_overlap = chunkOverlap
    )
    chunks = splitter.split_documents(documents)
    return chunks
