import sys
import csv
from pydriller import Repository
from tabulate import tabulate

# Define the table headers
columns = ["old_file path", "new_file path", "commit SHA", "parent commit SHA", 
           "commit message", "diff_myers", "diff_hist", "Matches"]

# Store commit information
rows = []
count = 0
last_n = 500

# Collect commits from the repository
commits = []
for x in Repository(sys.argv[1], only_no_merge=True, order="reverse").traverse_commits():
    if x.in_main_branch:
        count += 1
        commits.append(x)
        if count == last_n:
            break

# Reverse the order for proper commit sequence
commits.reverse()

# Process each commit
for commit in commits:
    for m in commit.modified_files:
        diff_myers = m.diff_parsed["added"] if "added" in m.diff_parsed else "N/A"
        diff_hist = m.diff_parsed["deleted"] if "deleted" in m.diff_parsed else "N/A"
        
        # Check if diff outputs match
        matches = "Yes" if diff_myers == diff_hist else "No"

        rows.append([
            m.old_path if m.old_path else "N/A",  
            m.new_path if m.new_path else "N/A",  
            commit.hash,
            commit.parents[0] if commit.parents else "N/A",  
            commit.msg,
            diff_myers,
            diff_hist,
            matches
        ])

# Print the table
print(tabulate(rows, headers=columns, tablefmt="grid"))

# Save to CSV
with open(sys.argv[1] + "_results/commits_info.csv", "a") as csvFile:
    writer = csv.writer(csvFile)
    writer.writerow(columns)
    writer.writerows(rows)