#coding:utf-8
import requests
import random
from locust import HttpLocust,TaskSet,task

class UserBehavior(TaskSet):

    def on_start(self):

        """ on_start is called when a Locust start before any task is scheduled """

        data = {"phone": "18621789040",
                "password": "Wzf123456",
                "captcha": "1111"}
        r = requests.post(
            url='http://172.16.41.94:7788/robin/data/sys/login',
            json=data,
        )
        self.token = r.json()['token']
        print("----初始化token----",self.token)
        list1 = []
        for i in range(10000):
            list1.append(i)
        choose_id = random.choice(list1)
        choose_id_sure = str(choose_id)
        msgid = "1235854d-c126-475a-b225-63f28d9b"
        self.msgID = msgid + choose_id_sure
        print("----初始化msgID----",self.msgID)
    def on_stop(self):
        print("----over----")

    @task(1)
    def test_charge_msg(self):
        #请求短信计费接口/charge/msg
        headers = {"Content-Type":"application/json"}
        data = {"apiAccount": "N4398498",
                "apiPlatForm": "01",
                "channel": "TDBM000006",
                "msgId": self.msgID,
                "number": 1,
                "productCode": "1001",
                "realChannel": "ZSJRH000006",
                "receiver": "18356061167",
                "submitTime": 1558331318000,
                "netWork":"local",
                "token":self.token}
        r = self.client.post(
            url='/charge/msg',
            headers=headers,
            json=data,catch_response=True
        )
        print(r.json())
        # assert r.status_code == 200
        with r as response:
            if response.status_code == 200:
                response.success()
            else:
                response.failure('Failed!')
        print("计费的token",self.token)
        print("计费的msgID",self.msgID)


class WebsiteUser(HttpLocust):
    task_set = UserBehavior
    host = "http://172.16.41.70:8082"
    min_wait = 3000
    max_wait = 6000

if __name__ == '__main__':
    import os
    os.system("locust -f test_sms_bill.py")