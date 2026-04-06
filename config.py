import os 
from dotenv import load_dotenv

load_dotenv()

GroqAPIKey = os.getenv("GROQ_API_KEY")
modelName = "llama-3.3-70b-versatile"
embeddingModel = "all-MiniLM-L6-v2"
chromaDIR = "chromaStore"
chunkSize = 500
chunkOverlap = 50