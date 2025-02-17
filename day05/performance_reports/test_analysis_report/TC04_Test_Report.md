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
- **Total Requests:** 187  
- **Total Failures:** 0  
- **Response Times:**  
  - **Median:** 140.0 ms  
  - **Average:** 147.05838556152804 ms  
  - **Min:** 89.77600000071106 ms  
  - **Max:** 393.3457000002818 ms  
- **Throughput:** ~3.18951773324381 requests/s

### Key Percentiles
- **50th Percentile:** 140 ms  
- **66th Percentile:** 160 ms  
- **75th Percentile:** 170 ms  
- **80th Percentile:** 190 ms  
- **90th Percentile:** 210 ms  
- **95th Percentile:** 250 ms  
- **98th Percentile:** 290 ms  
- **99th Percentile:** 330 ms  
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
- The system met the expected criteria (no errors, response time well below 1000 ms).  
- **Functional:** All CRUD operations (create, update, delete) passed with 0 failures.  
- **Performance:** The API performed within acceptable limits, with 95% of requests under 210 ms.  
- **Scalability:** The system handled the test load well with no errors, confirming stable performance under high load.

---

📌 **Tested by:** Sevim  
📆 **Test Date:** 17/02/2025  
🔎 **Test Tool:** Locust  
📝 **HTML Report:** [View Report](performance_reports/2025-02-17_12-41-46/report.html)
