import requests
import json

# url=r"https://mp.weixin.qq.com/mp/getappmsgext?" \
#     r"f=json&mock=&fasttmplajax=1&f=json&wx_header=1" \
#     r"&pass_ticket=IEp3CkWmapnkPbLWSotHpXKu8Skcbr9LnPOHCw1KNHstv1QxlgqX%252Bmsvb16y7VhL" #!!!!

url2=" https://mp.weixin.qq.com/mp/getappmsgext?" \
     "f=json&mock=&uin=777&key=777" \
     "&pass_ticket=IEp3CkWmapnkPbLWSotHpXKu8Skcbr9LnPOHCw1KNHstv1QxlgqX%25252Bmsvb16y7VhL&wxtoken=777" \
     "&devicetype=android-23&clientversion=2700033b" \
     "&appmsg_token=999_haML2si%252Fj3XbyB%252Fz7fKjeeu5Juv0v1ix6ZG_KojdJ44q4xi4rqrqZPpYuFU-4yU2I68teUR20wQoqByf" \
     "&x5=0&f=json "



data={
        '__biz':'MzI0MzMyMjQ4Nw'
        ,'appmsg_type':9
        ,'mid':2247485249
        ,'sn':'cf7afda7cc571322d49c9f5aeab2029b'
           ,'idx':1
            ,'devicetype':'android-23'
            ,'version':'2700033b'
            ,'is_need_ticket':0
            ,'is_need_ad':0
            ,'is_need_reward':0
              ,'is_only_read':1
            ,'pass_ticket':'IEp3CkWmapnkPbLWSotHpXKu8Skcbr9LnPOHCw1KNHstv1QxlgqX%252Bmsvb16y7VhL' #!!!!!!
}
headers={
 'User-agent': 'Mozilla/5.0 (Linux; Android 6.0.1; OPPO R9sk Build/MMB29M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/67.0.3396.87 XWEB/564 MMWEBSDK/190102 Mobile Safari/537.36 MMWEBID/897 MicroMessenger/7.0.3.1400(0x2700033B) Process/toolsmp NetType/WIFI Language/zh_CN MicroMessenger/7.0.3.1400(0x2700033B) Process/toolsmp NetType/WIFI Language/zh_CN'
 ,'X-WECHAT-KEY':'820cef1bf0d3a41182f3507653f1c75db41638643cc7c536b9a434ca70bf80b32d5ba88f4baa04cbbbfeeb8f6e97d8100a6a1af0d916e4682a9380656f4e47d492284fbf20bed2088198d209a0e08915'
 ,'X-WECHAT-UIN':'MTgyNjczMTc4Mg%3D%3D'
}
ret=requests.post(url2,verify=False,data=data,headers=headers)
print(ret.text)
# d1=json.loads(ret.text)
# like_num=d1['appmsgstat']["like_num"]
# read_num=d1['appmsgstat']["read_num"]
#
# print("喜欢数是%s"%like_num)
# print("阅读数是%s"%read_num)

