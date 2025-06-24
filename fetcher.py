import requests
from config import FREELANCER_API_BASE, SEARCH_KEYWORDS, MAX_RESULTS

def fetch_jobs():
    url = f"{FREELANCER_API_BASE}/projects/0.1/projects/active/"
    params = {
        "query": " ".join(SEARCH_KEYWORDS),
        "limit": MAX_RESULTS,
        "compact": "true",
        "job_details": "true"
    }
    response = requests.get(url, params=params)
    response.raise_for_status()
    return response.json().get("result", {}).get("projects", [])
