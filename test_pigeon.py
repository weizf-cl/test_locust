#coding:utf-8
from locust import HttpLocust, TaskSet, task

# 定义用户行为
class UserBehavior(TaskSet):
    @task
    def pigeon_index(self):
        self.client.get("/")

class WebsiteUser(HttpLocust):
    task_set = UserBehavior
    host = "http://172.16.41.37:9999"
    min_wait = 3000
    max_wait = 6000

if __name__ == '__main__':
    import os
    os.system("locust -f test_pigeon.py")