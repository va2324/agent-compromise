import os
from dotenv import load_dotenv
from langchain_openrouter import ChatOpenRouter
from langchain.tools import tool
from langchain.agents import create_agent
from langchain_community.tools import ShellTool

load_dotenv()

@tool
def load_skill(skill : str):
    """Load a specialized skill prompt. Return the skill's prompt and context."""
    path = f"./skills/{skill}/SKILL.md"
    if not os.path.exists(path):
        return f"Skill name {skill} not found!"
    with open(path, "r") as f:
        return f.read()
    
shell_tool = ShellTool()

model = ChatOpenRouter(model='', temperature=0)

tools = [load_skill, shell_tool]

system_prompt = """You are a virtual assistant. You can communicate with a database agent using terminal commands. 
                Use the load_skill tool to access the 'terminal' skill. Use the shell_tool to run necessary commands in the terminal."""

agent = create_agent(model=model, tools=tools, system_prompt=system_prompt)

while True:
        query = input("User: ")
        if query == "quit":
            print("Agent: Have a nice day!")
            break
        result = agent.invoke({"messages": [{"role": "user", "content": query}]})
        print(f"Agent: {result["messages"][-1].content}")