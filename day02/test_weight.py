from locust import TaskSet, constant, task, HttpUser


class MyHTTPCat(TaskSet):
    weight = 1  # This task runs less frequently compared to the other task

    @task
    def get_status(self):
        """User requests HTTP status 200"""
        self.client.get("/200")
        print("Get Status of 200")
        self.interrupt(reschedule=False)  # Stop execution of this task set and return to parent user class


class MyAnotherHTTPCat(TaskSet):
    weight = 3  # This task runs more frequently compared to MyHTTPCat

    @task
    def get_500_status(self):
        """User requests HTTP status 500"""
        self.client.get("/500")
        print("Get Status of 500")
        self.interrupt(reschedule=False)  # Stop execution of this task set and return to parent user class


class MyLoadTest(HttpUser):
    host = "https://http.cat"  # Target host for the test
    tasks = [MyHTTPCat, MyAnotherHTTPCat]  # Assign tasks for the user to execute
    wait_time = constant(1)  # Users wait 1 second between tasks

    ## RUN: locust -f day02\test_weight.py
