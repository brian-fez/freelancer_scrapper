from config import SEARCH_KEYWORDS
from llm import ask_llm

def compute_match_score(title: str, description: str) -> int:
    combined = (title + " " + description).lower()
    score = sum(kw.lower() in combined for kw in SEARCH_KEYWORDS)
    return int((score / len(SEARCH_KEYWORDS)) * 100)

def classify_job_type(title: str, description: str) -> str:
    prompt = f"""
Given the following job post:

Title: {title}
Description: {description}

Classify this job into one of the following categories:
1. Simple Automatable Job (can be automated with scripts or bots, no deep skills required)
2. Not Relevant

Respond with only one of these labels: "Simple Automatable Job", or "Not Relevant".
"""
    return ask_llm(prompt)
