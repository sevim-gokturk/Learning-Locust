# TC04 Test Execution Report

## Overview
- **Test Configuration:**  
  - Users: 10  
  - Spawn Rate: 2 users/sec  
  - Duration: 60s  
  - Locust File: `test_validateResponse.py`
- **Objective:** Evaluate API performance under load for user management operations (create, update, delete).

---

## Aggregated Metrics
- **Total Requests:** 195  
- **Total Failures:** 0  
- **Response Times:**  
  - **Median:** 110 ms  
  - **Average:** 127.16 ms  
  - **Min:** 86.18 ms  
  - **Max:** 385.08 ms  
- **Throughput:** ~3.32 requests/s

### Key Percentiles
- **50th Percentile:** 110 ms  
- **66th Percentile:** 120 ms  
- **75th Percentile:** 140 ms  
- **80th Percentile:** 150 ms  
- **90th Percentile:** 180 ms  
- **95th Percentile:** 210 ms  
- **98th Percentile:** 330 ms  
- **99th Percentile:** 360 ms  
- **99.9th Percentile:** 390 ms

---

## Endpoint Summary
- **POST /api/users:**  
  - Created new users with consistent response times (~130 ms).
- **PUT /api/users/{id}:**  
  - Updated user details; response times ranged between 104 ms and 385 ms (aggregated average ~127 ms).
- **DELETE /api/users/{id}:**  
  - Deleted users with stable performance (response times ~110-120 ms).

---

## Conclusion 
- **Test Outcome:** **PASSED** ✅
- The system **met** the expected criteria (no errors, response time well below 500 ms).
- **Functional:** All CRUD operations (create, update, delete) passed with 0 failures.
- **Performance:** The API performed within acceptable limits, with 95% of requests under 210 ms.
- **Scalability:** The system handled the test load well with no errors, confirming stable performance under moderate load.

> **Note:** Detailed per-endpoint results are available in the attached full report for further analysis.

---

📌 **Tested by:** Sevim
📆 **Test Date:** 17/02/2025 
🔎 **Test Tool:** Locust  
📝 **HTML Report:** [View Report](performance_reports/2025-02-17_12-41-46/report.html)