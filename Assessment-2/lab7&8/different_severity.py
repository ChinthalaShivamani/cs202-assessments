import json
import os
import pandas as pd
import matplotlib.pyplot as plt

# Get all Bandit reports
reports = sorted([f for f in os.listdir() if f.startswith("bandit_report_") and f.endswith(".json")])

severity_timeline = {
    "HIGH": [],
    "MEDIUM": [],
    "LOW": []
}

for report in reports:
    commit_hash = report.split("_")[-1].split(".")[0]
    commit_time = os.popen(f'git show -s --format=%ci {commit_hash}').read().strip()

    with open(report, "r") as file:
        try:
            data = json.load(file)
        except json.JSONDecodeError:
            continue

        for severity in ["HIGH", "MEDIUM", "LOW"]:
            count = sum(1 for issue in data.get("results", []) if issue["issue_severity"] == severity)
            if count > 0:
                severity_timeline[severity].append((commit_time, count))

# Convert to DataFrame
df_high = pd.DataFrame(severity_timeline["HIGH"], columns=["Date", "Count"])
df_medium = pd.DataFrame(severity_timeline["MEDIUM"], columns=["Date", "Count"])
df_low = pd.DataFrame(severity_timeline["LOW"], columns=["Date", "Count"])

for df in [df_high, df_medium, df_low]:
    df["Date"] = pd.to_datetime(df["Date"])
    df.sort_values("Date", inplace=True)

# Plot all severity levels
plt.figure(figsize=(12,6))
plt.plot(df_high["Date"], df_high["Count"], label="High Severity", marker='o', color='red')
plt.plot(df_medium["Date"], df_medium["Count"], label="Medium Severity", marker='s', color='orange')
plt.plot(df_low["Date"], df_low["Count"], label="Low Severity", marker='^', color='green')

plt.xlabel("Date")
plt.ylabel("Number of Vulnerabilities")
plt.title("Introduction and Fixing Trends for Different Severity Levels")
plt.legend()
plt.grid()
plt.xticks(rotation=45)
plt.show()