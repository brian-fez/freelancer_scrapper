from langchain.prompts import PromptTemplate
from llm import ask_llm

prompt_template = PromptTemplate(
    input_variables=["title", "description"],
    template="""
You are an expert freelance data scientist.

A client posted the following job:

Title: {title}
Description: {description}

Please:
1. Summarize the job
2. Outline how you would do it in 5 steps
3. Suggest tech stack
4. Estimate cost and duration
"""
)

def generate_job_plan(title: str, description: str) -> str:
    prompt = prompt_template.format(title=title, description=description)
    return ask_llm(prompt)
