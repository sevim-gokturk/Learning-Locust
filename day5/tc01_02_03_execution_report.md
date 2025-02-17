# **Test Execution Report - Reqres API**

## **Test Summary**
- **Test Date:** 17/02/2025
- **Total Test Cases Executed:** 3
- **Total Requests Sent:** 3
- **Total Failures:** 0
- **Overall Success Rate:** ✅ 100%

---

## **Test Case Results**

### **TC001 - Create a new user**
| **Test Case ID** | **Description** | **Expected Result** | **Actual Result** | **Status** | **Execution Time (ms)** |
|-----------------|----------------|---------------------|------------------|-----------|----------------------|
| TC001 | Create a new user | ✅ Response status = **201 Created** <br> ✅ Response contains a unique `id` <br> ✅ Response contains a valid `createdAt` timestamp | ✅ **Passed** <br> Status: **201 Created** <br> `id` returned, `createdAt` present | ✅ **Passed** | **281.05 ms** |

---

### **TC002 - Update user details**
| **Test Case ID** | **Description** | **Expected Result** | **Actual Result** | **Status** | **Execution Time (ms)** |
|-----------------|----------------|---------------------|------------------|-----------|----------------------|
| TC002 | Update user details | ✅ Response status = **200 OK** <br> ✅ `job` field is updated correctly | ✅ **Passed** <br> Status: **200 OK** <br> `job` updated successfully | ✅ **Passed** | **132.93 ms** |

---

### **TC003 - Delete a user**
| **Test Case ID** | **Description** | **Expected Result** | **Actual Result** | **Status** | **Execution Time (ms)** |
|-----------------|----------------|---------------------|------------------|-----------|----------------------|
| TC003 | Delete a user | ✅ Response status = **204 No Content** <br> ✅ User is removed successfully | ✅ **Passed** <br> Status: **204 No Content** <br> User deleted | ✅ **Passed** | **127.55 ms** |

---

📌 **Tested by:** Sevim
📆 **Test Date:** 17/02/2025 
🔎 **Test Tool:** Locust  
📝 **HTML Report:** [View Report](performance_reports/2025-02-17_12-23-40/report.html)
