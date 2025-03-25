import json
import os
import pandas as pd
import matplotlib.pyplot as plt

# Get all Bandit reports
reports = sorted([f for f in os.listdir() if f.startswith("bandit_report_") and f.endswith(".json")])

cwe_counts = {}

for report in reports:
    with open(report, "r") as file:
        try:
            data = json.load(file)
        except json.JSONDecodeError:
            continue

        for issue in data.get("results", []):
            cwe_id = issue.get("issue_cwe", {}).get("id")
            if cwe_id:
                cwe_counts[cwe_id] = cwe_counts.get(cwe_id, 0) + 1

# Convert to DataFrame
df_cwe = pd.DataFrame(cwe_counts.items(), columns=["CWE ID", "Count"])
df_cwe = df_cwe.sort_values("Count", ascending=False)

# Plot CWE frequency
plt.figure(figsize=(12,6))
plt.bar(df_cwe["CWE ID"].astype(str), df_cwe["Count"], color='skyblue')
plt.xlabel("CWE ID")
plt.ylabel("Frequency")
plt.title("Most Common CWEs in OSS Repositories")
plt.xticks(rotation=90)
plt.grid(axis='y')
plt.show()