# **Test Order and Prioritization in Locust**

## **1️⃣ Task Order: Random vs. Sequential**

### **🔹 Random Execution (`TaskSet`)**
In a `TaskSet`, Locust **randomly selects** a task after each execution.

```python
from locust import User, task, constant

class MyTest(User):
    wait_time = constant(1)  # 1-second wait between tasks

    @task(3)  # Higher weight, runs more often
    def browse(self):
        print("Browsing Products")
    
    @task(1)  # Lower weight, runs less often
    def checkout(self):
        print("Checking Out")
```
✅ **Browsing happens 3x more than Checkout**.

### **🔹 Sequential Execution (`SequentialTaskSet`)**
In a `SequentialTaskSet`, tasks **execute in a fixed order** every time.

```python
from locust import HttpUser, SequentialTaskSet, task, constant

class UserFlow(SequentialTaskSet):
    @task
    def home(self):
        print("Visiting Home Page")

    @task
    def browse(self):
        print("Browsing Products")

    @task
    def checkout(self):
        print("Checking Out")

class LoadTest(HttpUser):
    tasks = [UserFlow]
    wait_time = constant(1)
```
✅ **Users always follow the flow**: Home → Browse → Checkout.

---

## **2️⃣ Task Prioritization: Controlling Frequency**

### **🔹 Adjusting Task Weight**
Higher `@task(weight)` values **increase execution frequency**.

```python
@task(5)  # Runs 5x more than others
```

### **🔹 Controlling User Distribution**
Different user types can have different weights.

```python
class ShopperUser(HttpUser):
    weight = 5  # More shoppers
    tasks = [UserFlow]

class AdminUser(HttpUser):
    weight = 1  # Fewer admins
    tasks = [AdminFlow]
```
✅ **ShopperUser runs 5 times more than AdminUser**.

### **🔹 Adding Custom Delays**
Tasks can have **different wait times**.

```python
wait_time = between(1, 5)  # Waits between 1-5 sec before next task
```
✅ Simulates **realistic user behavior** with varied delays.

---

## **3️⃣ Choosing the Right Strategy**
| **Scenario**                  | **Use**               |
|--------------------------------|-----------------------|
| Simulate random user actions   | `TaskSet`            |
| Follow a strict user journey   | `SequentialTaskSet`  |
| Prioritize frequent tasks      | `@task(weight)`      |
| Control user mix               | `User weight`        |
| Add real-world delays          | `between(x, y)`      |


