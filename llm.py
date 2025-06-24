from langchain.chat_models import ChatOllama
from langchain.schema import HumanMessage
from config import OLLAMA_MODEL

llm = ChatOllama(model=OLLAMA_MODEL)

def ask_llm(prompt: str) -> str:
    response = llm([HumanMessage(content=prompt)])
    return response.content.strip()
