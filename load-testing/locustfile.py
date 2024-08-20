from locust import HttpUser, task

class HelloWorldUser(HttpUser):
    @task
    def hello_world(self):
        self.client.post("/", data={
            "auth_type": "email",
            #"phone": "+998919399689",
            "email": "admin@gmail.com",
        })
        #self.client.post("/")