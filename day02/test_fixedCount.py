from locust import HttpUser, task

class UserA(HttpUser):
    fixed_count = 10 # Fixed 10 users will be run
    @task
    def task_a(self):
        self.client.get("/endpoint_a")
# Run: locust -f day02\test_fixedCount.py
