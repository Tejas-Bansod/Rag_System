import os
from langchain_community.chat_models import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

def load_llm():
    return ChatOpenAI(
        model=os.getenv("DEFAULT_MODEL"),
        temperature=0.2,
        openai_api_key=os.getenv("OPENAI_API_KEY"),
        openai_api_base=os.getenv("OPENAI_API_BASE_URL"),
    )
