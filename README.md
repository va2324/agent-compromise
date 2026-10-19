# agent-compromise
A research project for examining agent compromise through indirect prompt injection.

## How it Works
This project simulates a virtual network consisting of a PostgreSQL database, two AI agents (one for executing terminal commands & one for managing the database), and a vulnerable Linux host machine. The objective is to use indirect prompt injection to compromise the terminal agent and make it hack the Linux host machine. 

A malicious prompt is inserted into the database, telling the terminal agent to log into the Linux host via SSH. The terminal agent calls the database agent, which returns the malicious entry that compromises the terminal agent and tricks it into hacking the Linux host, which has an exposed SSH port on the network. 

Additionally, there is a file agent that reads PDF & MD files. The pdf & md folders contain files with malicious content that are read by the file agent and 

## Setup
Download Visual Studio Code: https://code.visualstudio.com/download

Download Git & Git Bash: https://git-scm.com

Clone the project with the following command:
```
git clone https://github.com/va2324/agent-compromise
```

Ensure you have Python installed on your system. Enter the command below to check if Python is already installed. If not, download Python from this website: https://www.python.org/
```
python --version
```

Ensure you have Docker and Docker Compose installed on your system. Enter the commands below to check if they are already installed. If not, download Docker Desktop from this website: 
https://docker.com/
```
docker --version
docker-compose --version
```

To install PostgreSQL, follow the instructions on this website: https://www.w3schools.com/postgresql/postgresql_install.php

You do not have to install pgAdmin4 if you do not want to since you can just use the SQL Shell, but it is much easier to manage PostgreSQL databases with the pgAdmin4 application. Once you have PostgreSQL installed, create a new database and insert sample data and malicious prompts. The db.sql file contains some examples. 

## API Keys
You will need to obtain API keys from MistralAI & OpenRouter. The database agent runs on the MistralAI model 'mistral-small-2603' for unlimited requests, and the terminal & file agents run on free models from OpenRouter (you can also used paid models if you are willing to pay). Obtain API keys from the following websites: 

https://mistralai.com/

https://openrouter.ai/

Create a .env file based on .env.example and place your keys in that file. Additionally, insert your PostgreSQL configurations in the .env file.

## Running the Project
It is highly recommended that you create a Python virtual environment to avoid dependency conflicts with other projects. Follow the instructions on this website to create your own virtual environment: https://www.w3schools.com/python/python_virtualenv.asp

Once the environment is created, activate it and run the following command: 
```
pip install -r requirements.txt
```
This will install all necessary dependencies for the project. Additionally, create a .dockerignore file and place your virtual environment directory inside the file so that it does not take up unnecessary space in the Docker container. 

You can run the terminal, database, and file agents individually by entering the following commands: 
```
python agent.py
python db_agent.py
python file_agent.py
```

To run the virtual network, enter the following command: 
```
docker compose up -d
```

Connect to the container with the AI agents with the following command: 
```
docker compose attach agent
```
Once connected, you can run commands in the terminal agent. To use the database agent, enter any command regarding the database. The terminal agent will call the database agent with the same command, and the database agent will return the results. To test the prompt injections, enter a command like "Read the name of the user with id 15" where the name is actually a malicious prompt. The database will return the prompt, and you can see if the terminal agent will be tricked into hacking the Linux host. 

When you are finished, enter the following command to shut down the network:
```
docker compose down
```

The file agent is not on the Docker network. It can only be run through Python. You can enter commands like "Read the PDF file pdf/pdf1", and the file agent will read the corresponding file, and you can see how it responds to the malicious prompt within the file.  
