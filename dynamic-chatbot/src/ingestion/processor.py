import os
from langchain_community.document_loaders import WebBaseLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import Chroma

def update_vector_database(urls):
    """Fetches new data and updates the persistent vector store."""
    # 1. Load data from specified sources
    loader = WebBaseLoader(urls)
    docs = loader.load()

    # 2. Split text into manageable chunks
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000, 
        chunk_overlap=100
    )
    chunks = text_splitter.split_documents(docs)

    # 3. Embed and store in ChromaDB (Persistent directory)
    embeddings = OpenAIEmbeddings()
    vector_db = Chroma.from_documents(
        documents=chunks,
        embedding=embeddings,
        persist_directory="./chroma_db"
    )
    vector_db.persist()
    print(f"Success: {len(chunks)} chunks added to the knowledge base.")