from dotenv import load_dotenv
from langchain_ollama import ChatOllama


import os
load_dotenv()

llm = ChatOllama(temperature=0, model="gemma3:4b")

def main():
    print("Hello from langchain-course!")

if __name__ == "__main__":
    main()
