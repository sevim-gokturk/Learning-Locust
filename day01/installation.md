# Locust Performance Test

## Installation Guide

### 1. Install Python
Make sure you have Python installed on your computer.
- Check Python version:
  ```sh
  python --version
  ```
- If you do not have Python, download it from [python.org](https://www.python.org/)

### 2. Create Virtual Environment
A virtual environment keeps the project clean.
- On Windows:
  ```sh
  python -m venv locust-env
  locust-env\Scripts\activate
  ```
- On Mac/Linux:
  ```sh
  python3 -m venv locust-env
  source locust-env/bin/activate
  ```

### 3. Install Locust
After activating the virtual environment, install Locust:
```sh
pip install locust
```
Check if Locust is installed:
```sh
locust -V
```

### 4. Create Locust Test File
Create a new file called **locustfile.py** and copy this code:

```python
from locust import HttpUser, task, between

class MyUser(HttpUser):
    wait_time = between(1, 3)
    host = "http://example.com"

    @task
    def test_homepage(self):
        self.client.get("/")
```

### 5. Run Locust
Start Locust with this command:
```sh
locust
```
Open **http://localhost:8089** in your browser.

---
Locust is now ready to use! 🚀

