
import asyncio
import os

from autogen_agentchat.agents import AssistantAgent
from autogen_agentchat.ui import Console
from autogen_ext.models.openai import OpenAIChatCompletionClient
from dotenv import load_dotenv


api_key = os.getenv("OPENAI_API_KEY")

async def main():
    load_dotenv()
    api_key = os.getenv("OPENAI_API_KEY")

    if not api_key:
        raise ValueError(
            "OPENAI_API_KEY is not set. "
            "Please check your environment variables."
        )
    # Create the OpenAI model client
    model_client = OpenAIChatCompletionClient(
        model="gpt-4o-mini",
        api_key=api_key,
    )
    try:
        # Create the HR assistant
        agent = AssistantAgent(
            name="hr_assistant",
            model_client=model_client,
            system_message="You are an HR assistant.",
        )
        # Ask for exactly five bullet points
        task = (
            "Write a job description for a Junior Python Developer. "
            "Return exactly five bullet points, with one concise "
            "sentence per bullet. Do not include a title or introduction."
        )
        # Run the agent and display its response
        await Console(
            agent.run_stream(task=task)
        )
    finally:
        # Always close the model client
        await model_client.close()

if __name__ == "__main__":
    asyncio.run(main())
