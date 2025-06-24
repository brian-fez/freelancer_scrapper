from fetcher import fetch_jobs
from report import build_report, save_report

if __name__ == "__main__":
    print("🔍 Fetching jobs from Freelancer...")
    jobs = fetch_jobs()
    print(f"✅ {len(jobs)} jobs fetched. Classifying and analyzing...")

    report_df = build_report(jobs)

    if not report_df.empty:
        save_report(report_df)
    else:
        print("⚠️ No relevant jobs found.")
