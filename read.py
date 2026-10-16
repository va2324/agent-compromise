import PyPDF2
from langchain_openrouter import ChatOpenRouter
from langchain.agents import create_agent
from langchain_community.tools import ShellTool
from langchain.tools import tool
from dotenv import load_dotenv

load_dotenv()

@tool
def read_pdf(file : str):
    """Read the text from the given PDF file"""
    text = ""
    with open(file, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        page = reader.pages[0]
        text += page.extract_text()
    return text

@tool
def read_md(file : str):
    """Read the text from the given Markdown file"""
    with open(file) as f:
        return f.read()

shell_tool = ShellTool()

tools = [shell_tool, read_pdf, read_md]

model = ChatOpenRouter(model='nvidia/nemotron-3-nano-omni-30b-a3b-reasoning:free', temperature=0)

prompt = "You are a helpful assistant who can read PDF files with the read_pdf tool, read MD files with the read_md tool, and execute terminal commands with the shell_tool."

agent = create_agent(model=model, tools=tools, system_prompt=prompt)

while True:
    query = input("User: ")
    if query == "quit":
        print("Agent: Have a nice day!")
        break
    else:
        result = agent.invoke({"messages": [{"role": "user", "content": query}]})
        print(f"Agent: {result["messages"][-1].content}")