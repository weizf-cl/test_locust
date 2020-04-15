#coding:utf-8
# import requests
from locust import HttpLocust,TaskSet,task

class UserBehavior(TaskSet):
    @task(1)
    def test_api(self):
        #获取分页账户接口
        data = {"name": "WanShu",
                "signature": "fbad2e89aa4d3b5a2268b3dfda16cd21bc7899c9",
                "timestamp": "1535521846",
                "page": 1,
                "pageSize": 10,
                "type":1}
        r = self.client.post(
            url='/Api-Customer-getAccountList',
            data=data
        )
        # print(r.json())
        assert r.status_code == 200

class WebsiteUser(HttpLocust):
    task_set = UserBehavior
    host = "http://172.16.20.115"
    min_wait = 3000
    max_wait = 6000

if __name__ == '__main__':
    import os
    os.system("locust -f test_api.py")