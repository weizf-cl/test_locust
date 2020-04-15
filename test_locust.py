from locust import HttpLocust,TaskSet,task

class UserBehavior(TaskSet):
    @task
    def baidu_index(self):
        self.client.get("/")

class WebsiteUser(HttpLocust):
    task_set = UserBehavior
    host = "https://www.baidu.com"
    min_wait = 3000
    max_wait = 6000


if __name__ == '__main__':
    import os
    os.system("locust -f test_locust.py")
