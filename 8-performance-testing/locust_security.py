import random
from locust import HttpUser, task, between

class SecurityTestUser(HttpUser):
    wait_time = between(0.1, 1)

    # Run the task 3 times more often that usual
    @task(3)
    def valid_request(self):
        self.client.post("/add", json={"a": 10, "b": 20})

    @task(1)
    def sql_injection_attempt(self):
        payload = {"a": "SELECT * FROM users", "b": 5}

        with self.client.post("/add", json=payload, catch_response=True) as response:
            if response.status_code == 400:
                response.success()
            else:
                response.failure(f"Sanitation failed. Status: {response.status_code}")
    
    @task(1)
    def large_number_attack(self):
        payload = {"a": 1e30, "b": 1e30}
        with self.client.post("/multiply", json=payload, catch_response=True) as response:
            if response.status_code == 400:
                response.success()
            else:
                response.failure("Server failed to reject big numbers.")
    
    @task(1)
    def malformed_json(self):
        headers = {'Content-Type': 'application/json'}
        bad_json = '{"a"}: 10, "b": '
        with self.client.post("/add", data=bad_json, headers=headers, catch_response=True) as response:
            if response.status_code == 400:
                response.success()