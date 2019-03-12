import re
import json
import requests
class Wx_title:
    # def __init__(self,url):
    #     self.url=url

    def get_num(self):

        with open('log.txt',"rb+") as f:
            r=f.read().decode("utf-8")
            f.seek(0)
            f.truncate()

        re1=re.findall('\{.*\}',r)
        dic=json.loads(re1[0])
        print("阅读数是：%s 喜欢数是：%s "%(dic['appmsgstat']['read_num'],dic['appmsgstat']['like_num']))
        # print(dic['name'])
        # print(dic["read_num"],dic['like_num'])
        f.close()
if __name__=="__main__":
    w=Wx_title()
    w.get_num()