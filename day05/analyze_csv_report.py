import pandas as pd
import json
import os

# ==========================================
# CONFIGURATION VARIABLES
# ==========================================
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
CONFIG_FILE = os.path.join(BASE_DIR, "config.json")
# Use a relative path from BASE_DIR; adjust if needed.
CSV_FILE = os.path.abspath(os.path.join(BASE_DIR, "../day5/performance_reports/2025-02-17_13-24-21/report_stats.csv"))
OUTPUT_FILE = os.path.join(BASE_DIR, "TC05_Test_Report.md")

# ==========================================
# Function to Generate Test Execution Report
# ==========================================
def generate_tc_report(csv_file, config_file, output_file, test_case_id, objective, endpoint_summary, tested_by, test_date):
    # Load configuration from the JSON file
    if not os.path.exists(config_file):
        print(f"Error: Configuration file '{config_file}' not found!")
        return
    with open(config_file, "r", encoding="utf-8") as cf:
        config = json.load(cf)
    
    # Read the CSV file containing the aggregated test results
    if not os.path.exists(csv_file):
        print(f"Error: CSV file '{csv_file}' not found!")
        return
    df = pd.read_csv(csv_file)
    
    # Locate the aggregated row (assuming the "Name" column contains "Aggregated")
    aggregated = df[df.iloc[:, 1].astype(str).str.contains("Aggregated", na=False)]
    if aggregated.empty:
        print("Error: Aggregated row not found. Please verify your CSV file.")
        return
    agg = aggregated.iloc[0]
    
    # Extract metrics from the aggregated row (formatted to 3 decimal places)
    total_requests = agg['Request Count']
    total_failures = agg['Failure Count']
    median_rt = agg['Median Response Time']
    avg_rt = agg['Average Response Time']
    min_rt = agg['Min Response Time']
    max_rt = agg['Max Response Time']
    throughput = agg['Requests/s']
    
    perc50 = agg['50%']
    perc66 = agg['66%']
    perc75 = agg['75%']
    perc80 = agg['80%']
    perc90 = agg['90%']
    perc95 = agg['95%']
    perc98 = agg['98%']
    perc99 = agg['99%']
    perc99_9 = agg['99.9%']
    
    # Compute the HTML report link automatically from the CSV file directory
    computed_html_report_link = os.path.join(os.path.dirname(csv_file), "report.html")
    computed_html_report_link = computed_html_report_link.replace("\\", "/")  # Ensure forward slashes

    # Auto-calculate test outcome based on conditions:
    if total_requests == 0:
        auto_outcome = "NOT EXECUTED"
    elif total_failures > 0:
        auto_outcome = "FAILED"
    elif avg_rt < 1000:
        auto_outcome = "PASSED"
    else:
        auto_outcome = "BLOCKED"
    
    # Generate auto-calculated conclusion parts for Functional and Performance
    functional_text = "All CRUD operations passed with 0 failures." if total_failures == 0 else f"Some operations failed with {total_failures} failures."
    performance_text = "The API performed within acceptable limits, with 95% of requests under 210 ms." if perc95 < 210 else f"Performance issue: 95th percentile is {perc95:.3f} ms."
    
    # Create an HTML dropdown snippet using <details> for outcome options
    outcome_dropdown = """
<details>
  <summary>Click to view outcome options</summary>

- PASSED  
- FAILED  
- BLOCKED  
- NOT EXECUTED  
</details>
"""
    
    # Create the Markdown report content
    report = f"""# {test_case_id} Test Execution Report

## Overview
- **Test Configuration:**  
  - Users: {config['users']}  
  - Spawn Rate: {config['spawn_rate']} users/sec  
  - Duration: {config['duration']}  
  - Locust File: `{config['locust_file']}`
- **Objective:** {objective}

---

## Aggregated Metrics
- **Total Requests:** {total_requests}  
- **Total Failures:** {total_failures}  
- **Response Times:**  
  - **Median:** {median_rt:.3f} ms  
  - **Average:** {avg_rt:.3f} ms  
  - **Min:** {min_rt:.3f} ms  
  - **Max:** {max_rt:.3f} ms  
- **Throughput:** ~{throughput:.3f} requests/s

### Key Percentiles
- **50th Percentile:** {perc50:.3f} ms  
- **66th Percentile:** {perc66:.3f} ms  
- **75th Percentile:** {perc75:.3f} ms  
- **80th Percentile:** {perc80:.3f} ms  
- **90th Percentile:** {perc90:.3f} ms  
- **95th Percentile:** {perc95:.3f} ms  
- **98th Percentile:** {perc98:.3f} ms  
- **99th Percentile:** {perc99:.3f} ms  
- **99.9th Percentile:** {perc99_9:.3f} ms

---

## Endpoint Summary
{endpoint_summary}

---

## Conclusion 
- **Test Outcome:** {auto_outcome}  
  {outcome_dropdown}
- **Functional:** {functional_text}  
- **Performance:** {performance_text}  
- **Scalability:** [Please fill scalability details manually]

---

📌 **Tested by:** {tested_by}  
📆 **Test Date:** {test_date}  
🔎 **Test Tool:** Locust  
📝 **HTML Report:** [View Report]({computed_html_report_link})
"""
    # Write the report to the output Markdown file with UTF-8 encoding
    with open(output_file, "w", encoding="utf-8") as f:
        f.write(report)
    
    print(f"✅ Report successfully generated: {output_file}")

# ==========================================
# Example Usage
# ==========================================
objective = "Evaluate API performance under high concurrent load for user management operations (create, update, delete)."

endpoint_summary = """- **POST /api/users:**  
  - Created new users with consistent response times (~130 ms).
- **PUT /api/users/{id}:**  
  - Updated user details; response times ranged between 104 ms and 385 ms (aggregated average ~127 ms).
- **DELETE /api/users/{id}:**  
  - Deleted users with stable performance (response times ~110-120 ms)."""

# The "Test Outcome" dropdown and "Scalability" field are intended for manual input.
tested_by = "Sevim"
test_date = "17/02/2025"

# Generate the report using the CSV and configuration files
generate_tc_report(CSV_FILE, CONFIG_FILE, OUTPUT_FILE, "TC05", objective, endpoint_summary, tested_by, test_date)
