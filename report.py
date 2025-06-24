import pandas as pd
from datetime import datetime
from classifier import classify_job_type, compute_match_score
from planner import generate_job_plan

def build_report(jobs):
    rows = []
    for job in jobs:
        title = job['title']
        description = job['preview_description']
        job_type = classify_job_type(title, description)

        if job_type not in ["Data Scientist Job", "Simple Automatable Job"]:
            continue

        score = compute_match_score(title, description)
        plan = generate_job_plan(title, description)

        rows.append({
            "Job Title": title,
            "Job Type": job_type,
            "Match Score": score,
            "Budget": job.get('budget', {}).get('maximum', 'N/A'),
            "Posted": datetime.utcfromtimestamp(job['submitdate']).strftime("%Y-%m-%d"),
            "Plan": plan,
            "Job Link": f"https://www.freelancer.com/projects/{job['seo_url']}"
        })
    return pd.DataFrame(rows)

def save_report(df: pd.DataFrame):
    filename = f"freelancer_leads_{datetime.now().strftime('%Y%m%d_%H%M')}.xlsx"
    df.to_excel(filename, index=False)
    print(f"✅ Report saved to {filename}")
    print("\n📊 Job Type Distribution:")
    print(df["Job Type"].value_counts())
