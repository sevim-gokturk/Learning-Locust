
# **User Story**  
## **Title:** Performance and Validation Testing for User Management API  

**As a** system administrator,  
**I want** to create, update, and delete users via the Reqres API,  
**So that** I can ensure that user data is processed correctly and the system performs well under load.  

---  

# **User Acceptance Criteria (UAC)**  

✅ The system **must allow** creating a new user with a valid `name` and `job` fields.  
✅ The system **must return** a valid `id` and `createdAt` timestamp upon successful user creation.  
✅ The system **must allow** updating an existing user’s `job` field.  
✅ The system **must return** a `200 OK` response and update the user details correctly.  
✅ The system **must allow** deleting an existing user and return a `204 No Content` response.  
✅ API response times **must be under 1 second** for 95% of requests under normal load.  
✅ No **500 Internal Server Errors** should occur during load testing.  

---  

# **Test Cases with Expected Results**  

## **1️⃣ Functional Tests**  

| **Test Case ID** | **Description** | **Steps** | **Expected Result** |
|-----------------|----------------|-----------|---------------------|
| TC001 | Create a new user | 1. Send a `POST` request to `/api/users` with a valid `name` and `job`. | ✅ Response status = **201 Created** <br> ✅ Response contains a unique `id` <br> ✅ Response contains a valid `createdAt` timestamp |
| TC002 | Update user details | 1. Send a `PUT` request to `/api/users/{user_id}` with a new `job` value. | ✅ Response status = **200 OK** <br> ✅ `job` field is updated correctly |
| TC003 | Delete a user | 1. Send a `DELETE` request to `/api/users/{user_id}`. | ✅ Response status = **204 No Content** <br> ✅ User is removed successfully |

---  

## **2️⃣ Performance Tests**  

### **🚀 Load Test**  
✅ Simulate **real-world traffic** with different numbers of users.  
✅ Measure **response times (avg, min, max, p95, p99)**.  
✅ Ensure **no request fails due to server overload**.  

| **Test Case ID** | **Description** | **Users** | **Expected Result** |
|-----------------|----------------|------------|---------------------|
| TC004 | Test with **10 concurrent users** | 10 | ✅ No errors, response time < 500ms |
| TC005 | Test with **100 concurrent users** | 100 | ✅ No request failures, response time < 1s |
| TC006 | Test with **500 concurrent users (stress test)** | 500 | 🚨 Identify performance bottlenecks |

---  

### **🔥 Spike Test**  
✅ Simulate **sudden traffic spikes** (e.g., **Black Friday sales** scenario).  
✅ Check if the system **recovers quickly** after a spike.  

| **Test Case ID** | **Description** | **Users** | **Expected Result** |
|-----------------|----------------|------------|---------------------|
| TC007 | **Suddenly increase users from 10 → 500** in 5 sec | 10 → 500 | ✅ System does not crash, handles traffic spike |
| TC008 | **Suddenly drop users from 500 → 10** | 500 → 10 | ✅ System recovers without errors |

---  

### **🌊 Soak Test**  
✅ Simulate continuous traffic over a long period.  
✅ Detect **memory leaks** or **performance degradation**.  

| **Test Case ID** | **Description** | **Duration** | **Expected Result** |
|-----------------|----------------|-------------|---------------------|
| TC009 | **Run 100 users continuously for 1 hour** | 1 hour | ✅ System remains stable, no memory leaks |

---  

## **3️⃣ How to Execute These Tests?**  
💡 **Follow this step-by-step execution plan:**  

1️⃣ **Run a single-user test (`1 user`).**  
   ```sh
   locust -f day03\test_validateResponse.py --users 1 --spawn-rate 1 --headless
   ```  
   - **Check logs and ensure all operations work.**  
   - **Fix any issues before increasing load.**  

2️⃣ **Increase users to `10`, then `50`, then `100`**  
   ```sh
   locust -f day03\test_validateResponse.py --users 10 --spawn-rate 2 --headless
   ```  
   - Monitor **response times, error rates, and logs**.  

3️⃣ **Run a stress test (`500+ users`)**  
   ```sh
   locust -f day03\test_validateResponse.py --users 500 --spawn-rate 50 --headless
   ```  
   - Identify **system bottlenecks (database, API rate limits, etc.)**.  

4️⃣ **Perform a spike test**  
   - Simulate **sudden high load** and check how the system reacts.  

5️⃣ **Conduct a soak test**  
   - Run a **stable load for 1 hour** and check **memory usage, CPU load, and API stability**.  

---  

## **4️⃣ Key Metrics to Monitor**  
While running the tests, focus on **these performance indicators**:  

| **Metric** | **What It Means** | **Ideal Value** |
|------------|------------------|----------------|
| **Response Time (Avg, P95, P99)** | How fast the API responds | P95 < 1s, P99 < 2s |
| **Error Rate** | Percentage of failed requests | **< 1%** |
| **Throughput (Req/sec)** | How many requests API handles per second | High as possible |
| **CPU & Memory Usage** | Server health check | Stay within limits |

---  

## **🎯 Conclusion**  
🔹 Start small, analyze results, **increase load gradually**.  
🔹 Use **different test types** (load, stress, spike, soak).  
🔹 Monitor **key metrics** (response time, error rate, CPU usage).  
🔹 **Optimize bottlenecks** before scaling up to real traffic.  

