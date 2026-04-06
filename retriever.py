from langchain_huggingface import HuggingFaceEmbeddings
from langchain_chroma import Chroma
from config import embeddingModel, chromaDIR

def getRetriever(chunks = None):       #  yahan pa agar None add na krta to ye disk sa existing pichla project k chunks ly ata
    embeddings = HuggingFaceEmbeddings(model_name = embeddingModel)       # this help us to load the huggingfacemodel

    if chunks:
        vectorestore = Chroma.from_documents(
            documents = chunks,
            embedding = embeddings
        )
    else:
        vectorestore = Chroma(
            persist_directory = chromaDIR,
            embedding_function = embeddings
        )
    return vectorestore.as_retriever(search_kwarg = {"k" : 5})