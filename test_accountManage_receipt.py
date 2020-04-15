#coding:utf-8
# import requests
from locust import HttpLocust,TaskSet,task

class UserBehavior(TaskSet):
    @task(1)
    def test_accountManage_receipt(self):
        #财务管理-银行收款 查询接口
        data = {"name": "",
                "startTime":"1559318400000",
                "endTime":"1560959999999",
                "pageNo": 1,
                "pageSize": 10}
        r = self.client.post(
            url='/open/accountManage/receipt',
            data=data
        )
        # print(r.json())
        assert r.status_code == 200

class WebsiteUser(HttpLocust):
    task_set = UserBehavior
    host = "http://172.16.41.94:7788"
    min_wait = 3000
    max_wait = 6000

if __name__ == '__main__':
    import os
    os.system("locust -f test_accountManage_receipt.py")