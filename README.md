# Week5_Day1-AutoGen_HR_Assistant
# AutoGen HR Assistant — Week 5, Day 1

## 1. Project Overview

This project demonstrates how to build a basic AI agent using Microsoft's AutoGen framework and the OpenAI API.

The application creates an HR assistant that generates a job description for a Junior Python Developer. The response contains exactly five bullet points, with one concise sentence per bullet.

The project introduces the fundamentals of AI agents, asynchronous Python programming, model clients, and system messages.

## 2. Problem Statement

Build an `AssistantAgent` with the following requirements:

- Agent name: `hr_assistant`
- System message: `You are an HR assistant.`
- Model: `gpt-4o-mini`
- Task: Generate a five-bullet-point job description for a Junior Python Developer.
- Output: Display the response in the terminal using AutoGen's `Console`.
- Execution: Use `asyncio.run()` to execute the asynchronous main function.
- Security: Read the OpenAI API key from an environment variable loaded from a local `.env` file.
- Resource management: Close the model client after execution.

## 3. Technologies Used

| Technology | Purpose |
|---|---|
| Python | Programming language |
| AutoGen AgentChat | Creating and running the AI agent |
| AutoGen OpenAI Extension | Connecting to the OpenAI model |
| OpenAI API | Generating the job description |
| python-dotenv | Loading environment variables from `.env` |
| asyncio | Running asynchronous operations |

## 4. Project Structure

```text
Week5_Day1-AutoGen_HR_Assistant/
│
├── hr_agent.py
├── requirements.txt
├── .env
├── .gitignore
├── README.md
└── venv/
```

**File descriptions**

- `hr_agent.py` — Main Python application containing the AutoGen agent.
- `requirements.txt` — List of Python dependencies.
- `.env` — Stores the OpenAI API key locally.
- `.gitignore` — Prevents sensitive files and the virtual environment from being committed to Git.
- `README.md` — Project documentation.
- `venv/` — Python virtual environment containing the installed dependencies.

## 5. Prerequisites

Before running the application, ensure that you have:

1. Python installed.
2. An OpenAI API key.
3. Internet connectivity.
4. Access to the OpenAI API with available usage or billing as applicable.

A ChatGPT subscription does not automatically include OpenAI API credits.

## 6. Installation and Setup

### Step 1 — Open the project folder

Open PowerShell and navigate to the project directory.

```powershell
cd "D:\6. Training\Ai Dude - Agent training\Assignments\Week5_Day1-AutoGen_HR_Assistant"
```

Adjust the path if your project is stored elsewhere.

### Step 2 — Create a virtual environment

```powershell
python -m venv venv
```

Activate the environment:

```powershell
venv\Scripts\Activate.ps1
```

If PowerShell blocks activation, run:

```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy RemoteSigned
```

Then activate the environment again.

### Step 3 — Install dependencies

Create `requirements.txt` with the following contents:

```text
autogen-agentchat
autogen-ext[openai]
python-dotenv
```

Install the packages:

```powershell
python -m pip install --upgrade pip
pip install -r requirements.txt
```

Verify the installation:

```powershell
pip show autogen-agentchat
pip show autogen-ext
pip show python-dotenv
```

### Step 4 — Configure the OpenAI API key

Create a `.env` file in the project root.

Add the following line:

```text
OPENAI_API_KEY=your-actual-openai-api-key
```

Replace the example value with your actual API key.

Do not include the API key directly in the Python source code.

### Step 5 — Load the environment variable

The application uses `python-dotenv` to load the API key from `.env`.

At the beginning of `hr_agent.py`, import the required modules:

```python
import asyncio
import os

from dotenv import load_dotenv

from autogen_agentchat.agents import AssistantAgent
from autogen_agentchat.ui import Console
from autogen_ext.models.openai import OpenAIChatCompletionClient
```

Before reading the API key, call:

```python
load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")
```

This allows the application to read the key without requiring you to set it manually in PowerShell each time.

## 7. How the Application Works

### Step 1 — Load configuration

The application loads `.env` and reads the `OPENAI_API_KEY` environment variable.

If the key is missing, the application raises a clear error rather than attempting to run without credentials.

### Step 2 — Create the model client

`OpenAIChatCompletionClient` connects AutoGen to the selected OpenAI model.

```python
model_client = OpenAIChatCompletionClient(
    model="gpt-4o-mini",
    api_key=api_key,
)
```

### Step 3 — Create the HR assistant

The agent is created using `AssistantAgent`.

```python
agent = AssistantAgent(
    name="hr_assistant",
    model_client=model_client,
    system_message="You are an HR assistant.",
)
```

The system message defines the agent's role. It guides the model to respond as an HR assistant.

### Step 4 — Define the task

The task explicitly requests five bullet points, each containing one concise sentence.

```python
task = (
    "Write a job description for a Junior Python Developer. "
    "Return exactly five bullet points, with one concise "
    "sentence per bullet. Do not include a title or introduction."
)
```

Specifying the format reduces ambiguity in the generated response.

### Step 5 — Run the agent

AutoGen uses asynchronous execution to run the agent and display its streamed response.

```python
await Console(agent.run_stream(task=task))
```

### Step 6 — Close the model client

The application closes the model client when execution finishes.

```python
finally:
    await model_client.close()
```

Using `try/finally` ensures that cleanup is attempted even if an error occurs during agent execution.

### Step 7 — Start the asynchronous application

The script starts the event loop using:

```python
if __name__ == "__main__":
    asyncio.run(main())
```

This is the entry point of the application.

## 8. Run the Application

Ensure that your virtual environment is activated and that `.env` contains a valid API key.

Execute:

```powershell
python hr_agent.py
```

## 9. Expected Output

The wording may vary because the response is generated by an AI model.

```text
---------- TextMessage (hr_assistant) ----------
- Develop and maintain Python applications under the guidance of senior developers.
- Write clean, reusable, and well-documented Python code.
- Assist in debugging, testing, and resolving software issues.
- Work with APIs, databases, and version control tools such as Git.
- Collaborate with the development team to deliver reliable software solutions.
```

The assignment asks for exactly five bullet points. AutoGen may also display task-completion or streaming information in the terminal, depending on the installed version.

## 10. Troubleshooting

### Error: OPENAI_API_KEY is not set

**Cause:** The environment variable is missing or `.env` was not loaded.

**Solution:**

- Ensure `.env` is in the project root.
- Check that the variable is named exactly `OPENAI_API_KEY`.
- Confirm that `load_dotenv()` runs before `os.getenv("OPENAI_API_KEY")`.
- Make sure the file is named `.env`, not `.env.txt`.

### Error: Authentication or API key invalid

**Cause:** The key may be invalid, revoked, or incorrectly copied.

**Solution:**

- Verify the key in your OpenAI API account.
- Check for accidental spaces or quotation-mark issues.
- Never share the key in screenshots, source code, or public repositories.

### Error: ModuleNotFoundError

**Cause:** Dependencies may not be installed in the active Python environment.

**Solution:**

```powershell
venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
```

Run the script again after installation.

### Error: API quota or billing issue

**Cause:** The API account may not have available quota or valid billing configuration.

**Solution:** Check your API usage and billing settings. Installing Python packages does not provide API credits.

## 11. Security Best Practices

Create a `.gitignore` file with the following entries:

```text
.env
venv/
__pycache__/
*.py[cod]
```

This helps prevent accidental commits of API credentials and generated Python files.

Never commit `.env` to a public repository. If a key is accidentally exposed, revoke it and create a replacement.

## 12. Key Learning Outcomes

After completing this assignment, you should understand:

- How to create an `AssistantAgent` using AutoGen.
- How a system message influences an agent's behaviour.
- How to connect an agent to an OpenAI model.
- How to provide a task with explicit output requirements.
- Why AutoGen programs use asynchronous execution.
- How to display agent responses with `Console`.
- How to load secrets from environment variables.
- Why model clients should be closed after use.

## 13. Future Improvements

Possible extensions include:

- Allowing users to enter different job titles.
- Adding a Streamlit interface.
- Saving generated job descriptions to text or PDF files.
- Creating recruiter, interviewer, and HR-policy agents.
- Building a multi-agent workflow using sequential tasks.

These improvements are optional and are not required for the current assignment.

---

**Assignment:** Week 5, Day 1 — AutoGen HR Assistant  
**Framework:** Microsoft AutoGen  
**Language:** Python  
**Model:** GPT-4o mini

