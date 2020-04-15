#coding:utf-8
from locust import HttpLocust, TaskSet, task
from random import randint

# Robin__login性能测试-参数化
class UserBehavior(TaskSet):

    def on_start(self):
        users1 = ["18621789040", "18051294162","16601128367"]
        # for data in range(0, len(users1)):
        # a = int(len(users1))
        # data = randint(0, a-1)
        data = randint(0, int(len(users1))-1)
        print("选择的用户", users1[data])
        self.user_choose = users1[data]
        users2 = {"18621789040": "Wzf123456", "18051294162": "ibvans37", "16601128367": "dbigjd56"}
        self.password = users2[self.user_choose]
        print("选择的用户的密码", self.password)
        self.captcha = 1111
    def on_stop(self):
        print("---over---",self.user_choose)

    @task
    def login(self):
        data = {"phone":self.user_choose,
                "password":self.password,
                "captcha":self.captcha}
        r = self.client.post(
            url='/robin/data/sys/login',
            json=data,
            catch_response=True
        )
        # assert r.status_code == 200
        with r as response:
            if response.status_code == 200:
                response.success()
            else:
                response.failure('Failed!')
        print("登录成功的用户",self.user_choose)
        return r

class WebsiteUser(HttpLocust):
    task_set = UserBehavior
    host = "http://172.16.41.94:7788"
    min_wait = 1000
    max_wait = 3000

if __name__ == '__main__':
    import os
    os.system("locust -f test_parametric.py")