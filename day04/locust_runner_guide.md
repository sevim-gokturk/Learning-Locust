# Locust Performance Test Runner

This document provides instructions on setting up and using the **Locust Runner Script** (`run_performance_tests.py`) for performance testing.

## 📌 1. Create or Verify `config.json`

Ensure `config.json` exists in the **same directory** as the runner script:

```json
{
    "users": 100,
    "spawn_rate": 10,
    "duration": "2m",
    "locust_file": "your_script.py"
}
```

Modify this file to change test settings without editing the Python script.

## 📌 2. Running the Performance Tests

### ✅ Basic Run

Navigate to the test folder and execute:

```sh
python run_performance_tests.py
```

### ✅ Custom Run

Modify `config.json` and re-run:

```sh
python run_performance_tests.py
```

## 📌 3. Where Are the Reports?

After running tests, results are saved in:

```
performance_reports/YYYY-MM-DD_HH-MM-SS/
├── report.csv
├── report_failures.csv
├── report_exceptions.csv
└── report.html  <-- Opens automatically!
```
