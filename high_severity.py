import json
import os
import pandas as pd
import matplotlib.pyplot as plt

# Get all Bandit reports
reports = sorted([f for f in os.listdir() if f.startswith("bandit_report_") and f.endswith(".json")])

high_severity_timeline = []

for report in reports:
    commit_hash = report.split("_")[-1].split(".")[0]  # Extract commit hash
    commit_time = os.popen(f'git show -s --format=%ci {commit_hash}').read().strip()  # Get commit date

    with open(report, "r") as file:
        try:
            data = json.load(file)
        except json.JSONDecodeError:
            continue

        high_severity_count = sum(1 for issue in data.get("results", []) if issue["issue_severity"] == "HIGH")
        
        if high_severity_count > 0:
            high_severity_timeline.append((commit_time, high_severity_count))

# Convert to DataFrame
df = pd.DataFrame(high_severity_timeline, columns=["Date", "High Severity Count"])
df["Date"] = pd.to_datetime(df["Date"])
df = df.sort_values("Date")

# Plot the timeline
plt.figure(figsize=(10,5))
plt.plot(df["Date"], df["High Severity Count"], marker='o', linestyle='-')
plt.xlabel("Date")
plt.ylabel("Number of High Severity Vulnerabilities")
plt.title("High Severity Vulnerabilities Over Time")
plt.xticks(rotation=45)
plt.grid()
plt.show()
