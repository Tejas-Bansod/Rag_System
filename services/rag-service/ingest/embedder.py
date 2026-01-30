import os
from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import Chroma

assert os.getenv("OPENAI_API_KEY") is not None, "Please set OPENAI_API_KEY in .env"
assert os.getenv("OPENAI_API_BASE_URL") is not None, "Please set OPENAI_API_BASE_URL in .env"

def embed_documents(chunks):
    embeddings = OpenAIEmbeddings(
        openai_api_key=os.getenv("OPENAI_API_KEY"),
        openai_api_base=os.getenv("OPENAI_API_BASE_URL"),
    )
    db = Chroma(
        persist_directory="artifacts/indexes",
        embedding_function=embeddings
    )
    db.add_documents(chunks)
    db.persist()
