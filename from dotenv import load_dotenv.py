from dotenv import load_dotenv
import os
from langchain_ollama import ChatOllama
from langchain_core.messages import HumanMessage

load_dotenv()


def main():
    model_name = os.environ.get("OLLAMA_MODEL", "gemma3:4b")
    llm = ChatOllama(temperature=0, model=model_name)
    prompt = HumanMessage(content="What is the weather in the Oldambt?")
    response = llm.invoke([prompt])
    print("Hello from langchain-course!")
    print(response.content)


if __name__ == "__main__":
    main()