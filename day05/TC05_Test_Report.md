# TC05 Test Execution Report

## Overview
- **Test Configuration:**  
  - Users: 10  
  - Spawn Rate: 2 users/sec  
  - Duration: 60s  
  - Locust File: `test_CRUD.py`
- **Objective:** Evaluate API performance under high concurrent load for user management operations (create, update, delete).

---

## Aggregated Metrics
- **Total Requests:** 1802  
- **Total Failures:** 0  
- **Response Times:**  
  - **Median:** 100.000 ms  
  - **Average:** 121.284 ms  
  - **Min:** 78.627 ms  
  - **Max:** 553.410 ms  
- **Throughput:** ~30.561 requests/s

### Key Percentiles
- **50th Percentile:** 100.000 ms  
- **66th Percentile:** 110.000 ms  
- **75th Percentile:** 120.000 ms  
- **80th Percentile:** 130.000 ms  
- **90th Percentile:** 180.000 ms  
- **95th Percentile:** 210.000 ms  
- **98th Percentile:** 260.000 ms  
- **99th Percentile:** 350.000 ms  
- **99.9th Percentile:** 550.000 ms

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
- **Test Outcome:** PASSED  
  
<details>
  <summary>Click to view outcome options</summary>

- PASSED  
- FAILED  
- BLOCKED  
- NOT EXECUTED  
</details>

- **Functional:** All CRUD operations passed with 0 failures.  
- **Performance:** Performance issue: 95th percentile is 210.000 ms.  
- **Scalability:** [Please fill scalability details manually]

---

📌 **Tested by:** Sevim  
📆 **Test Date:** 17/02/2025  
🔎 **Test Tool:** Locust  
📝 **HTML Report:** [View Report](C:/Users/sevim/Desktop/LearningLocust/day5/performance_reports/2025-02-17_13-24-21/report.html)
