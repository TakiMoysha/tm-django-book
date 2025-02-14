from locust import HttpUser, between, task


class LoadTesting(HttpUser):
    def on_start(self):
        self.client.get("/api/health")

    @task
    def index(self):
        self.client.get("/api/orders")
