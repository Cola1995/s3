from wxpy import *
import time

note='''欢迎加入众阅社区，本社区是自动化互助社区，提供APP实现无需人工干预，自动执行，可实现阅读、关注、点好看、点广告，查看详细信息请访问:yungsc.com.
有任何问题可以在群内留言，本群不允许发任何类型的文章，避免骚扰大家。
'''
#from tuling import get_response
bot=Bot()
user=bot.friends(update=False) #全部好友信息
group=bot.groups(update=False) #全部群组信息（保存为联系人的群）
#print(group)
#group= ensure_one(bot.groups().search('微信测试'))
@bot.register(group)
def auto_reply(msg):
    if msg.type=='Note':
        print(msg.text)
        # new_user= re.findall('".+"', msg.text)
        # new_user_str=new_user[0][1:-1]
        # print(new_user_str)  # 切片
        # time.sleep(1)

        #if '邀请' or '分享的二维码加入群聊' in msg.text:
        if '邀请'  in msg.text or '分享的二维码加入群聊' in msg.text:

            time.sleep(1)
            print('新人进群')
            return note
    else:
        return
embed()
