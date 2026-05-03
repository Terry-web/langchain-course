from dotenv import load_dotenv 
load_dotenv()
#from asyncio import tools
#from lanngchain.agents import create_agent
# langchain-ollama
from langchain.chat_models import init_chat_model
from langchain_ollama import ChatOllama
from langchain.tools import tool
from langchain_core.messages import SystemMessage, HumanMessage, ToolMessage
from langsmith import traceable
max_iterations = 10
model = "llama3.1:8b" 

# --- Tools ( Langchain Tools ) ---
@tool
def get_weather(location: str) -> float:
    """Get the current weather for a given location."""
    # Here you would implement the logic to get the weather, e.g., call a weather API
    return f"The current weather in {location} is sunny with a temperature of 25°C."

@tool
def swarm_posibilities() -> str:
    """Get the current swarm possibilities."""
    # Here you would implement the logic to get swarm possibilities, e.g., call a beekeeping API
    return "The current swarm possibilities are low due to stable weather conditions."

# --- Agent Loop ---
@traceable(name="beekeeping_agent")
def run_agent(question: str):
    pass

if __name__ == "__main__":
    print("Welcome to the Beekeeping Assistant(.bind_tools)!")
    print()
    result = run_agent("What are the current swarm possibilities?")