from wxpy import *
import time
bot = Bot()
user_list = bot.groups(update=False,contact_only=False)
# print(user_list[1].name)
# print(user_list[1].members)
while True:
    time.sleep(10)
    # input(">>>")
    print(time.time())
    for i in range(len(user_list)):
        print("群聊名称:%s,群聊人数：%s"%(user_list[i].name,len(user_list[i])))
        print("群成员:%s"%user_list[i].members)
        # for j in user_list[i]:
        #     print(j)



