
from dotenv import load_dotenv

load_dotenv()
import os 
from langchain.agents import create_agent
from langchain.tools import tool 
from langchain_core.messages import SystemMessage, HumanMessage
from langchain_ollama import ChatOllama
from langchain_tavily import TavilySearch





llm = ChatOllama(temperature=0, model="llama3.1:8b")
tools = [TavilySearch(max_results=3)]
agent = create_agent(model=llm, tools=tools) 




def main():

    result = agent.invoke({
        "messages": [HumanMessage(content="For a place for the beekeeping basiscursus")]
    })

    print(result)

if __name__ == "__main__":
    main()