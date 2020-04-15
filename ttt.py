from random import randint
# users = {"18621789040": "Wzf123456", "user2": 123123, "user3": 111222}
# print(users["18621789040"])

users1 = ["user1","user2","user3"]
print(len(users1))
for i in range(0,len(users1)):
    print(i)
# data = randint(0, 2)
    print(users1[i])
    user_choose = users1[i]
    users2 = {"user1": "Wzf123456", "user2": 123123, "user3": 111222}
# data = randint(1, 3)
# print(data)
# username = "user" + str(data)
# print(username)
    password = users2[user_choose]
    print(password)
# captcha = 1111