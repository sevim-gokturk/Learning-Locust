from locust import HttpUser, task, constant, SequentialTaskSet


class MyTest(SequentialTaskSet):
    # This class defines the sequence of tasks each user follows.
    # Since it inherits from SequentialTaskSet, tasks will run in the exact order they are defined.
    # Each user will:
    #   1. Start the test (on_start)
    #   2. Browse a product (browse_product)
    #   3. Visit the cart page (cart_page)
    #   4. End the test (on_stop)
    def on_start(self):
        self.client.get("/", name=self.on_start.__name__)
        print("Start")

    @task
    def browse_product(self):
        self.client.get("/product/OLJCESPC7Z", name=self.browse_product.__name__)
        print("Browse Product")

    @task
    def cart_page(self):
        self.client.get("/cart", name=self.browse_product.__name__)
        print("Cart Page")

    def on_stop(self):
        self.client.get("/", name=self.on_stop.__name__)
        print("Stop")


class LoadTest(HttpUser):
    # This class represents the user type performing the test.
    # It assigns the sequential task set (MyTest) to users.
    # We separate this into a different class because:
    #   - MyTest defines WHAT users do (task behavior).
    #   - LoadTest defines HOW MANY users run and test settings.
    # This separation improves modularity and reusability.
    host = "https://onlineboutique.dev"
    tasks = [MyTest]
    wait_time = constant(1) # Each user waits 1 second between tasks.

    ## RUN: locust -f day01\test_sequentialTaskSet.py