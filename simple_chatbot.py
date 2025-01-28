import os

from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain.prompts import ChatPromptTemplate

from typing import Annotated

from typing_extensions import TypedDict

from langgraph.graph import StateGraph, START, END
from langgraph.graph.message import add_messages

load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")

#Added a test to verify if the OpenAI API key is loaded correctly.
"""if api_key:
    print("OpenAI API key loaded successfully.")
else:
    print("Error: OpenAI API key is not loaded.")"""