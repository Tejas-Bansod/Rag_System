import os
from dotenv import load_dotenv
from langchain_community.vectorstores import Chroma
from langchain_openai.embeddings import OpenAIEmbeddings

load_dotenv()

def get_vector_store():
    embeddings = OpenAIEmbeddings(
        openai_api_key=os.getenv("LANGCHAIN_API_KEY"),
        openai_api_base=os.getenv("OPENROUTER"),
    )

    return Chroma(
        persist_directory="artifacts/indexes",
        embedding_function=embeddings
    )
