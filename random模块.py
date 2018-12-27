import random
import time

r=random.randint(1,5) #整形1<=r<=5
random.randrange(1,5) #不包括5
random.choice([11,22,33]) #随机选取列表中的元素
random.sample([11,22,33],2) #随机选取列表中两个元素
random.uniform(1,3) #随机浮点数
random.shuffle([11,22,33]) #元素打乱
print(r)


# def code():
#     res=''
#     for i in range(5):
#         num=random.randint(0,9)
#         sss=chr(random.randint(65,122))
#         t=str(random.choice([num,sss]))
#         res+=t
#     return res
#
# if __name__=="__main__":
#     while True:
#         time.sleep(0.1)
#         print(code())