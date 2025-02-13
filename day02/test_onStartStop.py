from locust import HttpUser, task, constant, SequentialTaskSet


class MyTest(SequentialTaskSet):

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
    host = "https://onlineboutique.dev"
    tasks = [MyTest]
    wait_time = constant(1)

## RUN: locust -f day02\test_onStartStop.py


'''
on_start:  
Automatically executed once when the user's session is started.  
Purpose: To perform the necessary steps to prepare the user for testing.  
Examples:  
- Logging in the user.  
- Loading a page at the beginning.  
- Initializing a setting to be used during the test.  

on_stop:  
Automatically executed once when the user's session ends.  
Purpose: To perform the necessary actions to properly terminate the user's session.  
Examples:  
- Logging the user out of the system.  
- Clearing data created during the test.  
- Closing the user's session.  

'''