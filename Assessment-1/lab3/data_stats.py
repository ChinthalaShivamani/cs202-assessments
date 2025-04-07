import pandas as pd
import matplotlib.pyplot as plt

# Load CSV file path
file_path = "lab_3/commits_info.csv"

# Load the dataset
try:
    data = pd.read_csv(file_path)
except FileNotFoundError:
    print(f"Error: File not found at '{file_path}'. Please check the path.")
    exit()

code_extensions = {".py", ".java", ".cpp", ".js", ".cs", ".go", ".rs", ".kt", ".ts", ".c", ".h"}

def is_code_artifact(file_path):
    if isinstance(file_path, str):
        return any(file_path.endswith(ext) for ext in code_extensions)
    return False

# Categorize entries
data["artifact_type"] = data["old_file path"].apply(lambda x: "Code" if is_code_artifact(x) else "Non-Code")

# Count statistics
stats = {
    "Matches for non-code artifacts": len(data[(data["artifact_type"] == "Non-Code") & (data["Matches"] == "Yes")]),
    "No matches for non-code artifacts": len(data[(data["artifact_type"] == "Non-Code") & (data["Matches"] == "No")]),
    "Matches for code artifacts": len(data[(data["artifact_type"] == "Code") & (data["Matches"] == "Yes")]),
    "No matches for code artifacts": len(data[(data["artifact_type"] == "Code") & (data["Matches"] == "No")]),
}

# Plot the statistics
plt.figure(figsize=(10, 6))
bars = plt.bar(stats.keys(), stats.values(), color=["blue", "orange", "green", "red"])

# Add labels to each bar
for bar in bars:
    yval = bar.get_height()
    plt.text(bar.get_x() + bar.get_width() / 2, yval + 5, str(yval), ha="center", va="bottom")

plt.title("Dataset Statistics for Code and Non-Code Artifacts")
plt.xticks(rotation=0, ha="right")
plt.ylabel("Count")
plt.show()

