import sys
from pathlib import Path

sys.path.append("..")

from langchain.agents import create_agent
from common_config import llm_connect

def get_weather(city: str) -> str:
    """Get weather for a given city."""
    return f"It's always sunny in {city}!"


agent = create_agent(
    model=llm_connect(model="gpt-5.4-mini"),
    tools=[get_weather],
    system_prompt="You are a helpful assistant",
)

# Run the agent
result = agent.invoke(
    {"messages": [{"role": "user", "content": "What is the weather in San Francisco?"}]}
)
print(result["messages"][-1].content)