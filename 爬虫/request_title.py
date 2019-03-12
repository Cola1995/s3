import requests
url='https://mp.weixin.qq.com/s?__biz=MzI0MzMyMjQ4Nw==&mid=2247485249&idx=1&sn=cf7afda7cc571322d49c9f5aeab2029b&chksm=e96f9c59de18154f4072b19b774a96b31b1017b2d4b9698429a2e82fd8de0dec2299396f8d9a&scene=0&xtrack=1&key=addd0f5b003aa35941c26aafad0716e6df06e423d3fac78a505552c715252441efc50d195f052fce9c13fc40ea7b1dbe839bbd409c233f38dacbf7f61d668861209de8a0b2131e00e78ad6da78c25aba&ascene=1&uin=MTgyNjczMTc4Mg%3D%3D&devicetype=Windows+7&version=62060619&lang=zh_CN&pass_ticket=60ndXUmKi7Wv%2BhJQxpotZHQcTBRapO%2FFRQHIGAhzO%2F29GSKuZJHwndkCkjoQ0NBq&winzoom=1'

url1='http://mp.weixin.qq.com/s?__biz=MzI0OTc0MzAwNA==&mid=2247484527&idx=1&sn=7d3e4c9bbdea70b3839007eacfdd0101&chksm=e98d979cdefa1e8aabf4e04487d5502acc5d3429475e3f85607ec6fd0f7408d5c9fbd0acc816&scene=0&xtrack=1&key=addd0f5b003aa35941c26aafad0716e6df06e423d3fac78a505552c715252441efc50d195f052fce9c13fc40ea7b1dbe839bbd409c233f38dacbf7f61d668861209de8a0b2131e00e78ad6da78c25aba'


headers={
# "User-Agent":"Mozilla/5.0 (Linux; Android 6.0.1; MX4 Build/MOB30M) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/37.0.0.0 Mobile MQQBrowser/6.8 TBS/036849 Safari/537.36 MicroMessenger/6.3.27.880 NetType/WIFI Language/zh_CN"
"User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36 MicroMessenger/6.5.2.501 NetType/WIFI WindowsWechat QBCore/3.43.901.400 QQBrowser/9.0.2524.400"
,"Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8"
,
}



ret=requests.get(url1,verify=False,headers=headers)
print(ret.text)