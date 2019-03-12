import requests
import json


class Like_count():
    def __init__(self,pass_ticket,biz,mid,sn,key):
        self.pass_ticket=pass_ticket
        self.biz=biz
        self.mid=mid
        self.sn=sn
        self.key=key



    def start(self):

        url=r"https://mp.weixin.qq.com/mp/getappmsgext?" \
            r"f=json&mock=&fasttmplajax=1&f=json&wx_header=1" \
            r"&pass_ticket={0}".format(self.pass_ticket)



        data={
                '__biz':self.biz
                ,'appmsg_type':9   #喜欢数用
                ,'mid':self.mid
                ,'sn':self.sn
                   ,'idx':1
                    ,'devicetype':'android-23'
                    ,'version':'2700033b'
                    ,'is_need_ticket':0
                    ,'is_need_ad':0
                    ,'is_need_reward':0
                      ,'is_only_read':1
                    ,'pass_ticket':self.pass_ticket
        }
        headers={
         'User-agent': 'Mozilla/5.0 (Linux; Android 6.0.1; OPPO R9sk Build/MMB29M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/67.0.3396.87 XWEB/564 MMWEBSDK/190102 Mobile Safari/537.36 MMWEBID/897 MicroMessenger/7.0.3.1400(0x2700033B) Process/toolsmp NetType/WIFI Language/zh_CN MicroMessenger/7.0.3.1400(0x2700033B) Process/toolsmp NetType/WIFI Language/zh_CN'
         ,'X-WECHAT-KEY':self.key
         ,'X-WECHAT-UIN':'MTgyNjczMTc4Mg%3D%3D'

        }
        ret=requests.post(url,verify=False,data=data,headers=headers)
        d1=json.loads(ret.text)
        like_num=d1['appmsgstat']["like_num"]
        read_num=d1['appmsgstat']["read_num"]

        print("喜欢数是%s"%like_num)
        print("阅读数是%s"%read_num)
if __name__=="__main__":
    pass_ticket='A5Fr9JF7Dt2l1rtta62NCUMScelNWDZ35K1poJCKYbZ0AXTNBZ1X1Zspr8PgwoXg'
    biz='MzIwOTcyNjI0Nw=='

    sn='b26e2c4361de542c19d62b983a5093d4'
    key='1de87a9cefa179c45cb320bafa9b9dd7ce1cfaa3071b975017e1a652f3b5957ff03e1ef16b226cb3ee6ee8de2a915334f7fb82f31839f71cf4559004690fec6f8c5dc8d03a61e58341f7739264c46b62'
    l=Like_count(pass_ticket,biz,mid,sn,key)
    l.start()
#pass_ticket、_biz、mid、sn、X-WECHAT-KEY 必须通过fillter抓取
