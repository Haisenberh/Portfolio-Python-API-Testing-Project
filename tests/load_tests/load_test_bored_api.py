from locust import FastHttpUser, task, constant


class WebSiteUser(FastHttpUser):
    # simulated users wait 1 second after each task
    host = "https://www.boredapi.com"
    wait_time = constant(1)

    @task()
    def check_activity_api(self):
        url = "/api/activity/"
        result = self.client.get(url)
        if result.status_code is not "200":
            print(f"Got error response: {result.status_code}")
