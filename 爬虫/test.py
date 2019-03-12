import requests
import json

url=r"https://mp.weixin.qq.com/mp/getappmsgext?" \
    r"f=json&mock=&fasttmplajax=1&f=json&wx_header=1" \
    r"&pass_ticket=IEp3CkWmapnkPbLWSotHpXKu8Skcbr9LnPOHCw1KNHstv1QxlgqX msvb16y7VhL"

cc={
     "sd_userid":"12641551586253497",
    "sd_cookie_crttime" : "1551586253497",
 "pgv_pvid" : "597960080",
 "devicetype": "android-23",
 "version" : "2700033b",
    "lang" : "zh_CN"

}

data={




        '__biz':'MzUxMDk1NDU5Mw=='
        ,'appmsg_type':9   #喜欢数用
        ,'mid':2247483905
        ,'sn':'d7ad50aaec42837784f1c04756b2122d'
           ,'idx':1
            ,'devicetype':'android-23'
            ,'version':'2700033b'
            ,'is_need_ticket':0
            ,'is_need_ad':0
            ,'is_need_reward':0
              ,'is_only_read':1
            ,'pass_ticket':'IEp3CkWmapnkPbLWSotHpXKu8Skcbr9LnPOHCw1KNHstv1QxlgqXmsvb16y7VhL'
}
headers={
 'User-agent': 'Mozilla/5.0 (Linux; Android 6.0.1; OPPO R9sk Build/MMB29M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/67.0.3396.87 XWEB/564 MMWEBSDK/190102 Mobile Safari/537.36 MMWEBID/897 MicroMessenger/7.0.3.1400(0x2700033B) Process/toolsmp NetType/WIFI Language/zh_CN MicroMessenger/7.0.3.1400(0x2700033B) Process/toolsmp NetType/WIFI Language/zh_CN'
 ,'X-WECHAT-KEY':'c51d5110156248bce9446013cd3ecd7c280b394c7e2c252ba93e2d3020344c59e85bc519d6a16c74c8f1509bd59aeadeff6b3ed2a63b417e1b6f5c9f4984727df49f3f3f9230ac9e9f79c551ab22381b'
 ,'X-WECHAT-UIN':'MTgyNjczMTc4Mg%3D%3D'
}
ret=requests.post(url,verify=False,data=data,headers=headers)
d1=json.loads(ret.text)
like_num=d1['appmsgstat']["like_num"]
read_num=d1['appmsgstat']["read_num"]

print("喜欢数是%s"%like_num)
print("阅读数是%s"%read_num)

#pass_ticket、_biz、mid、sn、X-WECHAT-KEY 必须通过fillter抓取
