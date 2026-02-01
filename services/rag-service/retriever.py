from vectorstores import Chroma
from langchain_community.vectorstores import OpenAIEmbeddings
from dotenv import load_dotenv
import os

load_dotenv()

def retrieve(query, k=4):
    embeddings = OpenAIEmbeddings(
        openai_api_key=os.getenv("OPENAI_API_KEY"),
        openai_api_base=os.getenv("OPENAI_API_BASE_URL"),
    )
    db = Chroma(
        persist_directory="artifacts/indexes",
        embedding_function=embeddings
    )
    return db.similarity_search(query, k=k)
