🛠️ Freelancer Job Scraper & Analyzer

This project fetches active job listings from Freelancer.com, classifies them using a local LLM (via Ollama), and generates a detailed report of:

🧠 Data Science jobs

🤖 Simple automatable jobs (like data entry, PDF to CSV, etc.)

✅ Features

Keyword-based job scraping from Freelancer.com API

AI-driven classification of job type:

Data Scientist Job

Simple Automatable Job

Not Relevant

LLM-generated action plan for each relevant job

Exports results to an Excel report

Fully modular and easily extendable

📁 File Structure

freelancer_scraper/
├── main.py              # Entry point
├── config.py            # Constants like keywords and model name
├── fetcher.py           # Job fetching logic
├── classifier.py        # Matching and classification logic
├── planner.py           # LLM job plan generation
├── report.py            # Report building and export
├── llm.py               # LLM interface via ChatOllama
├── requirements.txt     # Python dependencies
└── README.md

🚀 Getting Started

1. 🧱 Prerequisites

Python 3.8+

Ollama installed and running with a model like llama3

llama3 pulled via Ollama:

ollama pull llama3

2. 📦 Install Python Dependencies

pip install -r requirements.txt

▶️ Usage

Run the tool:

python main.py

After a few seconds, you will get an Excel report like:

freelancer_leads_20250624_1032.xlsx

The report includes:

Job Title

Job Type

Match Score

Budget

Post Date

LLM-Generated Plan

Job URL

⚙️ Configuration

You can customize:

SEARCH_KEYWORDS: In config.py — add or remove skill terms

MAX_RESULTS: Number of jobs to fetch

OLLAMA_MODEL: Change to another local model if needed

🧠 Example Job Classifications

Title

Job Type

"Copy paste names into Excel"

Simple Automatable Job

"Design marketing banners"

Not Relevant

📌 Notes

Uses local models via Ollama

Designed to be LLM-agnostic — just adjust llm.py if using another interface.

Safe to run periodically to find freelance leads.

📮 Contact

Maintained by: Brian
Feel free to suggest improvements or contribute.