#coding:utf-8
import requests
import random
#登录获取token
def test_login():
    data = {"phone": "18621789040",
            "password": "Wzf123456",
            "captcha": "1111"}
    r = requests.post(
        url='http://172.16.41.94:7788/data/sys/login',
        json=data,
    )
    token = r.json()['token']
    return token

def choose_end_msgid():
    list1 = []
    for i in range(10000):
        list1.append(i)
    choose_id = random.choice(list1)
    #     choose_id = list1[i]
    choose_id_sure = str(choose_id)
    return choose_id_sure

#获取msgID
def choose_msgID1():
    msgid = "1235854d-c126-475a-b225-63f28d9b"
    i = choose_end_msgid()
    msgID = msgid + i
    return msgID

#选择成功或失败状态
def choose_suc_fail():
    suc_fail = ["success","failed"]
    suc_fail_sure = random.choice(suc_fail)
    return suc_fail_sure

# if __name__ == '__main__':
    # choose_end_msgid()
    # choose_msgID()