from dotenv import load_dotenv

load_dotenv()
from langchain.agents import create_agent
from langchain.tools import tool 
from langchain_core.messages import SystemMessage, HumanMessage
from langchain_ollama import ChatOllama
@tool
def search(query: str) -> str:
    """Tool that searches for the weather in the Oldambt"""
    
    print(f"Searching for {query}")
    return "Oldambt weather is sunny"
    


llm = ChatOllama(temperature=0, model="gemma3:4b")
tools = [search]
agent = create_agent(model=llm, tools=tools) 


def main():
    print("Hello from langchain-course!")
    result = agent.invoke(
        {
            "messages": HumanMessage(
                content="What is the weather in the Oldambt?"
                )
        }
    )
    print(result)

if __name__ == "__main__":
    main()
