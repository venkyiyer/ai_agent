from langchain_ollama import ChatOllama
from dotenv import load_dotenv
from ollama import Client
import os

load_dotenv()

os.environ["LANGSMITH_TRACING"] = "true"
os.environ["LANGSMITH_API_KEY"] = os.getenv("LANGSMITH_API_KEY")
os.environ["OLLAMA_API_KEY"] = os.getenv("OLLAMA_API_KEY")
os.environ["LANGSMITH_PROJECT"] = os.getenv("LANGSMITH_PROJECT")


llm = ChatOllama(
    model="gpt-oss:120b",
    base_url="https://ollama.com",
    client_kwargs={
        "headers": {"Authorization": "Bearer " + os.environ["OLLAMA_API_KEY"]}
    },
)

for chunk in llm.stream("Who is Cristiano Ronaldo?"):
    print(chunk.content, end="", flush=True)