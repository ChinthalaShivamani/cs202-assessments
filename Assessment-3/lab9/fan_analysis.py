import json
import csv
from pathlib import Path

# Load the dependencies JSON file with full path
dependency_file = "/home/set-iitgn-vm/lab9/click/src/click/dependencies.json"
with open(dependency_file, "r") as f:
    dependencies = json.load(f)

# Calculate fan-in and fan-out metrics
results = []
for module, data in dependencies.items():
    fan_in = len(data.get("imported_by", []))
    fan_out = len(data.get("imports", []))
    
    # Calculate instability metric (0 to 1, higher means more unstable)
    # I = fan-out / (fan-in + fan-out)
    total = fan_in + fan_out
    instability = fan_out / total if total > 0 else 0
    
    results.append({
        'module': module,
        'fan_in': fan_in,
        'fan_out': fan_out,
        'instability': instability
    })

# Sort results by module name for consistency
results.sort(key=lambda x: x['module'])

# Write to CSV file
output_file = Path("dependency_metrics.csv")
with open(output_file, "w", newline="") as csvfile:
    fieldnames = ['module', 'fan_in', 'fan_out', 'instability']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    
    writer.writeheader()
    for row in results:
        writer.writerow(row)

print(f"Metrics saved to {output_file.absolute()}")

# Optional: Print summary statistics
total_modules = len(results)
avg_fan_in = sum(r['fan_in'] for r in results) / total_modules
avg_fan_out = sum(r['fan_out'] for r in results) / total_modules
max_fan_in = max(results, key=lambda x: x['fan_in'])
max_fan_out = max(results, key=lambda x: x['fan_out'])

print(f"\nSummary Statistics:")
print(f"Total modules analyzed: {total_modules}")
print(f"Average fan-in: {avg_fan_in:.2f}")
print(f"Average fan-out: {avg_fan_out:.2f}")
print(f"Module with highest fan-in: {max_fan_in['module']} ({max_fan_in['fan_in']})")
print(f"Module with highest fan-out: {max_fan_out['module']} ({max_fan_out['fan_out']})")