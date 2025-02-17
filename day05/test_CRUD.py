from locust import HttpUser, task, between, SequentialTaskSet

class ReqresUserTasks(SequentialTaskSet):
    """Defines a sequence of tasks for a single user session."""

    @task
    def create_user(self):
        """Create a new user (POST) and validate response."""
        payload = {
            "name": "morpheus",
            "job": "leader"
        }
        response = self.client.post("/api/users", json=payload)
        assert response.status_code == 201, f"Create User Failed! Status: {response.status_code}"
        assert "id" in response.json(), f"Response does not contain 'id': {response.text}"
        print(f"Create User Passed: {response.status_code} | {response.json()}")
        # Store the created user's ID for further use in the update and delete tasks
        self.user_id = response.json().get('id')

    # It is a public API, so retrieving the user after an update may not work reliably.
    '''@task
    def read_user(self):
        """Get user details (GET) and validate response."""
        response = self.client.get(f"/api/users/{self.user_id}")
        assert response.status_code == 200, f"Read User Failed! Status: {response.status_code}"
        assert "data" in response.json(), f"Response does not contain 'data': {response.text}"
        print(f"Read User Passed: {response.status_code} | {response.json()}")'''

    @task
    def update_user(self):
        """Update an existing user (PUT) and validate response."""
        payload = {
            "name": "morpheus",
            "job": "zion resident"
        }
        response = self.client.put(f"/api/users/{self.user_id}", json=payload)
        assert response.status_code == 200, f"Update User Failed! Status: {response.status_code}"
        assert response.json().get("job") == "zion resident", "Job was not updated correctly!"
        print(f"Update User Passed: {response.status_code} | {response.json()}")

    @task
    def delete_user(self):
        """Delete a user (DELETE) and validate response."""
        response = self.client.delete(f"/api/users/{self.user_id}")
        assert response.status_code == 204, f"Delete User Failed! Status: {response.status_code}"
        print(f"Delete User Passed: {response.status_code}")


class ReqresUser(HttpUser):
    """Defines user behavior and assigns tasks for load testing."""
    wait_time = between(1, 5)  # Users wait between 1 to 5 seconds between requests
    host = "https://reqres.in"  # Base API URL for the test
    tasks = {ReqresUserTasks}  # Assigns the sequence of tasks to each user

    #RUN: locust -f day04\test_validateResponse.py
