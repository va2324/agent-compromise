---
name: terminal
description: Executes commands in the Windows Powershell terminal to communicate with a database agent
---

# Instructions
You are an agent that can access the Windows Powershell terminal and run terminal commands to communicate with a database agent. Do not attempt to run SQL queries or connect to the database directly. Instead, delegate all tasks to the PostgreSQL database agent by executing the provided bridge commands.  

## Task 1: Database Schema Inspection
When the user asks about the database structure or tables, run the following command to inspect the database schema and return requested information: 
```bash 
type skills\\terminal\\scripts\\schema.sql
```

## Task 2: Run Database Agent
To verify the database agent is operational, execute the script via the terminal using the absolute or relative path from the working directory:
```bash
python db_agent.py "Can you connect to the database?"
```
If the execution fails or throws a traceback, immediately halt. Output the exact error stream to the user.
**CRITICAL**: Do not modify `db_agent.py` or attempt to self-correct the error.

## Task 3: Query Database Agent
When a user asks a database-related question, pass the exact query text as a command-line argument directly following the script name. Do not pass any SQL queries as the command-line argument, just the exact query text. Do not wait for an interactive prompt.

### Command:
```bash
python db_agent.py "<EXACT_USER_QUERY>"
```