import json
import os
from collections import defaultdict

# Get all Bandit report files
reports = [f for f in os.listdir() if f.startswith("bandit_report_") and f.endswith(".json")]

# Data storage
summary = {}

for report in reports:
    commit_hash = report.split("_")[-1].split(".")[0]  # Extract commit hash
    with open(report, "r") as file:
        try:
            data = json.load(file)
        except json.JSONDecodeError:
            print(f"Skipping invalid JSON: {report}")
            continue

        high_severity = 0
        medium_severity = 0
        low_severity = 0

        high_confidence = 0
        medium_confidence = 0
        low_confidence = 0

        unique_cwes = set()

        for issue in data.get("results", []):
            # Count severity levels
            severity = issue.get("issue_severity", "UNKNOWN")
            if severity == "HIGH":
                high_severity += 1
            elif severity == "MEDIUM":
                medium_severity += 1
            elif severity == "LOW":
                low_severity += 1

            # Count confidence levels
            confidence = issue.get("issue_confidence", "UNKNOWN")
            if confidence == "HIGH":
                high_confidence += 1
            elif confidence == "MEDIUM":
                medium_confidence += 1
            elif confidence == "LOW":
                low_confidence += 1

            # Collect unique CWEs
            cwe_id = issue.get("issue_cwe", {}).get("id")
            if cwe_id:
                unique_cwes.add(cwe_id)

        # Store results per commit
        summary[commit_hash] = {
            "severity": {"HIGH": high_severity, "MEDIUM": medium_severity, "LOW": low_severity},
            "confidence": {"HIGH": high_confidence, "MEDIUM": medium_confidence, "LOW": low_confidence},
            "cwes": list(unique_cwes)
        }

# Save results to a JSON file
with open("bandit_summary.json", "w") as outfile:
    json.dump(summary, outfile, indent=4)

print("Analysis complete! Results saved in bandit_summary.json")