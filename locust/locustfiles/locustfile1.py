from locust import HttpUser, task, between


class LocustUser(HttpUser):

    # Method that returns the time (in seconds) between the execution of locust tasks.
    wait_time = between(1, 5)

    @task
    def demo_test(self):
        self.client.get("http://test.k6.io")
