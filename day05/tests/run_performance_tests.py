import os
import json
import subprocess
from datetime import datetime
import webbrowser

# Load configuration from config.json
def load_config():
    config_path = "config.json"
    if not os.path.exists(config_path):
        print("❌ Error: Config file not found! Make sure 'config.json' exists.")
        exit(1)
    
    with open(config_path, "r") as file:
        return json.load(file)

# Function to create a timestamped report directory
def create_report_directory():
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    report_dir = os.path.join("../performance_reports", timestamp)
    os.makedirs(report_dir, exist_ok=True)
    return report_dir

# Function to run Locust in headless mode
def run_locust(config, report_dir):
    users = config["users"]
    spawn_rate = config["spawn_rate"]
    duration = config["duration"]
    locust_file = config["locust_file"]

    print(f"🚀 Running Locust with {users} users, {spawn_rate}/sec spawn rate, for {duration}...")

    locust_cmd = [
        "locust",
        "-f", locust_file,
        "--headless",
        f"--users={users}",
        f"--spawn-rate={spawn_rate}",
        f"--run-time={duration}",
        f"--csv={os.path.join(report_dir, 'report')}",
        f"--html={os.path.join(report_dir, 'report.html')}"
    ]

    try:
        subprocess.run(locust_cmd, check=True)
        print(f"✅ Test completed! Reports saved in: {report_dir}")

        # Open the HTML report automatically
        html_report = os.path.join(report_dir, "report.html")
        if os.path.exists(html_report):
            webbrowser.open(html_report)

    except subprocess.CalledProcessError as e:
        print(f"❌ Error running Locust: {e}")

# Main function
def main():
    config = load_config()
    report_dir = create_report_directory()
    run_locust(config, report_dir)

if __name__ == "__main__":
    main()
