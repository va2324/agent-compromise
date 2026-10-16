import os
import sys
import asyncio
from dotenv import load_dotenv
from mcp_use import MCPClient, MCPAgent
from langchain_mistralai import ChatMistralAI

load_dotenv()

async def main():
    config = {
        "mcpServers": {
            "postgres": {
                "command": "npx",
                "args": ["-y", "@modelcontextprotocol/server-postgres", os.getenv("DB_LINK")]
            }
        },
    }

    client = MCPClient.from_dict(config)

    llm = ChatMistralAI(model_name='mistral-small-2603', temperature=0)
    
    system_prompt = "You are a PostgreSQL database agent. You execute SQL queries and return data in response to the user's prompts."

    agent = MCPAgent(llm, client, system_prompt, max_steps=100)

    if len(sys.argv) > 1:
        query = " ".join(sys.argv[1:])
        result = await agent.run(query, max_steps=100)
        print(f"Agent: {result}")
    else:
        while True:
            query = input("User: ")
            if query == "quit":
                print("Agent: Have a nice day!")
                break
            result = await agent.run(query, max_steps=100)
            print(f"Agent: {result}")


if __name__ == "__main__":
    asyncio.run(main())