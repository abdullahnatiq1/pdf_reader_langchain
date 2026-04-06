# PDF reader langchain

A RAG-based PDF question answering app built with LangChain and Groq.
Upload any PDF, ask questions about it, and get real-time streaming answers
powered by llama-3.3-70b-versatile. Built using LangChain's LCEL pipeline
with ChromaDB for vector storage and HuggingFace embeddings.

## Features

- Load any PDF from local path or web URL
- Semantic search using HuggingFace embeddings
- Real-time streaming responses
- Persistent vector storage with ChromaDB — no re-indexing on every run
- Powered by llama-3.3-70b-versatile via Groq

# Get Started

## Prerequisties

we need Groq API Key for this project

## Setting up Environment

first create .env file in the root of this project and add GROK_API_KEY

```
GROQ_API_KEY=YOUR_GROQ_API_KEY
```

## Create and Activate Virtual Environment

```
python -m venv .venv
.venv\Scripts\activate
```

## Install dependencies

```
pip install -r requirements.txt
```
