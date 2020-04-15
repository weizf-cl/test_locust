#coding:utf-8
import requests

def test_login():
    data = {"phone": "18621789040",
            "password": "Wzf123456",
            "captcha": "1111"}
    r = requests.post(
        url='http://172.16.41.94:7788/data/sys/login',
        json=data,
    )
    # print(r.json())
    # print(r.json()['token'])
    token = r.json()['token']
    return token
if __name__ == '__main__':
    test_login()