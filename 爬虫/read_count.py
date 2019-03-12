import requests
import json

url=r"https://mp.weixin.qq.com/mp/getappmsgext?" \
    r"f=json&mock=&fasttmplajax=1&f=json&wx_header=1" \
    r"&pass_ticket=ZZ7XT6GEzXBNjtPqxD+p2UF/H+3EsG97wGZE6it+9HA+9ca6F2p+3Yr3CoQmfhnY"

cc={
     "sd_userid":"12641551586253497",
    "sd_cookie_crttime" : "1551586253497",
 "pgv_pvid" : "597960080",
 "devicetype": "android-23",
 "version" : "2700033b",
    "lang" : "zh_CN"

}

data={

      'fasttmplajax':1
        ,'wx_header':1
        ,'pass_ticket':'ZZ7XT6GEzXBNjtPqxD p2UF/H3EsG97wGZE6it9HA9ca6F2p3Yr3CoQmfhnY',
        # 'f':json,
        # 'f':json,
        'mock':'',
        'r':0.009010642422378146
        ,'__biz':'MzU4NjYwODc5MQ=='
        ,'appmsg_type':9
        ,'mid':2247486671
        ,'sn':'61c5a2e57fa42e85591f03894ece1949'
          ,'idx':1,'scene':0,
        'title':'%E6%94%B6%E5%85%A5%E4%B8%8D%E9%AB%98%E7%9A%84%E6%97%B6%E5%80%99%EF%BC%8C%E6%99%9A%E4%B8%8A%E5%BA%94%E8%AF%A5%E8%AF%BB%E4%B9%A6%E5%AD%A6%E4%B9%A0%E8%BF%98%E6%98%AF%E5%85%BC%E8%81%8C%E8%B5%9A%E9%92%B1%EF%BC%9F'
            ,'ct':1551943800
            ,'devicetype':'android-23'
            ,'abtest_cookie':''
            ,'version':'2700033b'
            ,'is_need_ticket':0
            ,'is_need_ad':0
            ,'comment_id':710509442386771970
            ,'is_need_reward':0
            ,'send_time':''
            ,'both_ad':0
            ,'reward_uin_count':0
            ,'msg_daily_idx':1
            ,'is_original':0
            ,'is_only_read':1
            ,'pass_ticket':'ZZ7XT6GEzXBNjtPqxD%252Bp2UF%252FH%252B3EsG97wGZE6it%252B9HA%252B9ca6F2p%252B3Yr3CoQmfhnY'
            ,'is_temp_url':0
            ,'item_show_type':0
            ,'tmp_version':1
            ,'more_read_type':0
            ,'appmsg_like_type':2

}
headers={


 'Accept-Encoding': 'gzip',
             # 'User-Agent': 'Mozilla/5.0 AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.132 '
'User-agent': 'Mozilla/5.0 (Linux; Android 6.0.1; OPPO R9sk Build/MMB29M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/67.0.3396.87 XWEB/564 MMWEBSDK/190102 Mobile Safari/537.36 MMWEBID/897 MicroMessenger/7.0.3.1400(0x2700033B) Process/toolsmp NetType/WIFI Language/zh_CN MicroMessenger/7.0.3.1400(0x2700033B) Process/toolsmp NetType/WIFI Language/zh_CN'
,'X-WECHAT-KEY':'c44ffc707b0689fccd4eb215049a16e817646282b3d22d785386bea1a2aecb403ef800ae74d16e454b2dfb637bc458792fe04c6e76492a41ff86c0f5d9e75ae426448365c92db5fd14f36eaa2cfa88f1'
,'X-WECHAT-UIN':'MTgyNjczMTc4Mg%3D%3D'
}
ret=requests.post(url,verify=False,data=data,headers=headers,cookies=cc)
d1=json.loads(ret.text)
like_num=d1['appmsgstat']["like_num"]
read_num=d1['appmsgstat']["read_num"]

print("喜欢数是%s"%like_num)
print("阅读数是%s"%read_num)

