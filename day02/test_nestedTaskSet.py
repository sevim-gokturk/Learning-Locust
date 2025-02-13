from locust import TaskSet, constant, task, HttpUser


class MyHTTPCat(TaskSet):
    """
    This TaskSet simulates a user making a request to /200.
    After executing the request, the user stops due to `interrupt(reschedule=False)`,
    meaning they will NOT switch to another task set.
    """

    @task
    def get_status(self):
        self.client.get("/200")  # Sends a GET request to /200
        print("Get Status of 200")
        self.interrupt(reschedule=False)  # Stops execution without assigning a new task set


class MyAnotherHTTPCat(TaskSet):
    """
    This TaskSet simulates a user making a request to /500.
    Just like MyHTTPCat, the user stops after executing this task.
    """

    @task
    def get_500_status(self):
        self.client.get("/500")  # Sends a GET request to /500
        print("Get Status of 500")
        self.interrupt(reschedule=False)  # Stops execution without assigning a new task set


class MyLoadTest(HttpUser):
    """
    This class defines the test user behavior.
    Each user is randomly assigned to either MyHTTPCat or MyAnotherHTTPCat.
    Since each task set stops after one request, the test continuously spawns new users to maintain the load.
    """

    host = "https://http.cat"  # Target website
    tasks = [MyHTTPCat, MyAnotherHTTPCat]  # Assigning both task sets
    wait_time = constant(1)  # Each user waits 1 second before starting

    ## RUN: locust -f day02\test_nestedTaskSet.py
