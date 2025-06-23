# Automated Node.js Development Crew

This project leverages a crew of AI agents, powered by CrewAI, to automate the creation of a complete Node.js project from a high-level description. The agents collaborate to handle everything from project scaffolding and code generation to configuration and testing.

## Overview

The core of this project is a multi-agent system designed to mimic a software development team. You provide a description of a Node.js application, and the AI crew takes over, performing the necessary tasks to build out the project structure and write the code. This project uses large language models from Groq and Google for code generation and reasoning, and securely manages API keys by prompting the user on the first run.

## Features

- **Automated Project Scaffolding**: Creates the entire directory and file structure for a standard Node.js project.
- **AI-Driven Code Generation**: Agents write code for server logic, API routes, and more based on the project description.
- **Multi-Agent Collaboration**: Different agents with specialized roles (Project Manager, Developer, Tester) work together to complete the project.
- **Secure API Key Management**: No hardcoded keys. The application prompts you for API keys once per session and uses them in memory.
- **Extensible Toolset**: Comes with tools for executing command-line instructions, writing files, and leveraging LLMs for complex tasks.

## How It Works: The Crew

The project is built around a team of specialized AI agents, each with a distinct role and set of tools.

### The Agents

- **ProjectManagerAgent**:
  - **Goal**: Oversee and coordinate the creation of the Node.js project structure.
  - **Backstory**: An experienced technical project manager skilled in Node.js architecture and best practices.

- **CoreDeveloperAgent**:
  - **Goal**: Implement the core server functionality and main application logic.
  - **Backstory**: A senior Node.js developer specializing in server-side architecture and Express.js.

- **APIDevAgent**:
  - **Goal**: Create and implement API routes and controllers.
  - **Backstory**: An API specialist with deep knowledge of RESTful principles and Node.js routing.

- **TestingAgent**:
  - **Goal**: Implement comprehensive test suites for the application.
  - **Backstory**: A QA engineer specialized in Node.js testing methodologies.

- **ConfigurationAgent**:
  - **Goal**: Set up project configuration, environment settings, and Docker files.
  - **Backstory**: A DevOps engineer specialized in Node.js application configuration.

### The Tools

The agents use a powerful set of tools to accomplish their tasks:

- **CMD Tool** (`tools/cmd_tool.py`): Allows agents to execute any Windows CMD command, enabling them to create directories, initialize npm, and run scripts.
- **File Creation Tool** (`tools/create_files.py`): A tool to write generated code to specific files within the project structure.
- **LLM Tool** (`tools/LLM_tool.py`): A powerful tool that leverages a Groq LLM to generate code for project files based on the project architecture and a high-level description.
- **Web Scrapping Tool** (`tools/web_scrapping.py`): Uses Serper for web searches to gather information or examples if needed.

## Getting Started

Follow these steps to get your automated development crew up and running.

### Prerequisites

- Python 3.10 or higher
- An internet connection

### Installation

1.  **Clone the repository:**
    ```bash
    git clone
    cd AI-NodeJs
    ```

2.  **Install the dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

### Configuration

This project handles API keys securely. You do not need to create a `.env` file or hardcode any keys.

On the first run, the application will prompt you in the terminal to enter the necessary API keys for the services it uses (Groq, Google Gemini, Serper). These keys are stored in memory for the duration of the session only and will not be written to any file.

## Usage

1.  **Define Your Project**: Open the `tasks.py` file and modify the `Project` variable to describe the Node.js application you want to build.

    ```python
    # in tasks.py
    Project ="""
    The project is creating 3 end points one shows Hi, the other take from the url the 2 numbers and shows the sum, the 3th one take the 2 numbers from the url and shows the multiplication of them.
    """
    ```

2.  **Run the Crew**: Execute the main application file to kick off the development process.

    ```bash
    python main.py
    ```
    *(Note: You may need to create a `main.py` to initialize and run your CrewAI crew if one doesn't exist yet.)*

3.  **Monitor the Process**: The agents will log their progress to the console, and you can find detailed reports in the generated markdown files (`report.md`, `setup_report.md`, etc.).

## Project Structure

```
├── agents.py           # Defines the AI agents and their roles.
├── tasks.py            # Defines the tasks for the agents to execute.
├── configs.py          # Manages LLM models and secure API key handling.
├── tools/              # Contains custom tools for the agents.
│   ├── cmd_tool.py
│   ├── create_files.py
│   └── LLM_tool.py
├── requirements.txt    # Project dependencies.
└── README.md           # This file.
```