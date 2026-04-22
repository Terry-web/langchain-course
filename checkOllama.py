from dotenv import load_dotenv
from langchain_ollama import ChatOllama
import requests
import os

load_dotenv()


def check_ollama():
    try:
        res = requests.get("http://localhost:11434")
        if res.status_code == 200:
            print("✅ Ollama draait")
            return True
    except requests.exceptions.ConnectionError:
        pass

    print("❌ Ollama draait NIET. Start met: ollama serve")
    return False


def main():
    if not check_ollama():
        return

    llm = ChatOllama(
        model="gemma3:4b",
        temperature=0
    )

    response = llm.invoke("Zeg hallo in het Nederlands")
    print(response)


if __name__ == "__main__":
    main()