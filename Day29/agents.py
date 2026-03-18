from langchain_groq import ChatGroq
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Initialize the LLM with Groq
llm = ChatGroq(
    model="llama-3.3-70b-versatile",
    groq_api_key=os.getenv("GROQ_API_KEY")
)

# Planner Agent
planner_prompt = PromptTemplate(
    input_variables=["task"],
    template=""" 
You are a planning agent.
Break the task into clear steps.

Task: {task}

Steps:
"""
)

planner_agent = LLMChain(llm=llm, prompt=planner_prompt)

# Research Agent
research_prompt = PromptTemplate(
    input_variables=["steps"],
    template="""
You are a research agent.
Use the steps to gather useful information.

Steps:
{steps}

Research:
"""
)

research_agent = LLMChain(llm=llm, prompt=research_prompt)

# Writer Agent
writer_prompt = PromptTemplate(
    input_variables=["research"],
    template="""
You are a writer agent.
Write a structured report and Estimated cost based on the research.

Research:
{research}

Report:
"""
)

writer_agent = LLMChain(llm=llm, prompt=writer_prompt)