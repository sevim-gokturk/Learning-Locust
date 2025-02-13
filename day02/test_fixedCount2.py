from locust import HttpUser, task, constant, SequentialTaskSet

# This script runs 5 users in parallel (fixed_count = 5).
# Each user follows the tasks sequentially (on_start → browse_product → cart_page → on_stop).
# However, users are independent, meaning different users may be at different steps at the same time.
# Example: User 1 might be at cart_page, while User 2 is still browsing a product.
# This ensures a continuous and realistic load on the system.

class MyTest(SequentialTaskSet):

    def on_start(self):
        # A startup message for each user
        print(f"User {self.user.user_id} started")
        self.client.get("/", name="on_start")
    
    @task
    def browse_product(self):
        # Simulating a user browsing products
        print(f"User {self.user.user_id} is browsing products")
        self.client.get("/product/OLJCESPC7Z", name="browse_product")
    
    @task
    def cart_page(self):
        # Simulating a user visiting the cart page
        print(f"User {self.user.user_id} is visiting the cart")
        self.client.get("/cart", name="cart_page")
    
    def on_stop(self):
        # A message when each user finishes
        print(f"User {self.user.user_id} finished the test")
        self.client.get("/", name="on_stop")


class LoadTest(HttpUser):
    host = "https://onlineboutique.dev"
    tasks = [MyTest]
    wait_time = constant(1)
    fixed_count = 5  # Fixed number of 5 users will run
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Assigning a unique ID to each user
        if not hasattr(self.environment, "user_counter"):
            self.environment.user_counter = 0
        self.environment.user_counter += 1
        self.user_id = self.environment.user_counter  # Assign a unique ID to each user

## RUN: locust -f day02\test_fixedCount2.py --headless -u 5 -r 1