import requests
import json
import datetime
import time
import pymysql

class WxMps(object):
    """微信公众号文章、评论抓取爬虫"""

    def __init__(self, _biz, _pass_ticket, _app_msg_token, _cookie, _offset=0):
        self.offset = _offset
        self.biz = _biz  # 公众号标志
        self.msg_token = _app_msg_token  # 票据(非固定)
        self.pass_ticket = _pass_ticket  # 票据(非固定)
        self.headers = {
            'Cookie': _cookie,  # Cookie(非固定)
            'User-Agent': 'Mozilla/5.0 AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.132 '
            # 'x-wechat-key':'f8dcdb51042604497511aee52785d5f401429d6345a8f9590990ce55584df138eed6e293889b65baf20b2a767975a38537635027170dbd5c545a90ae4c16a4709717cc82d6b0b5654c9283e0b2a7ad7'
            # ,'x-wechat-uin' :'MTgyNjczMTc4Mg%3D%3D'
        }



    def start(self):
        """请求获取公众号的文章接口"""

        offset = self.offset
        while True:
            api = 'https://mp.weixin.qq.com/mp/profile_ext?action=getmsg&__biz={0}&f=json&offset={1}' \
                  '&count=10&is_ok=1&scene=124&uin=777&key=777&pass_ticket={2}&wxtoken=&appmsg_token' \
                  '={3}&x5=1&f=json'.format(self.biz, offset, self.pass_ticket, self.msg_token)

            resp = requests.get(api, headers=self.headers,verify=False).json()
            ret, status = resp.get('ret'), resp.get('errmsg')  # 状态信息
            if ret == 0 or status == 'ok':
                print(api)
                offset = resp['next_offset']  # 下一次请求偏移量
                general_msg_list = resp['general_msg_list']
                msg_list = json.loads(general_msg_list)['list']  # 获取文章列表
                for msg in msg_list:
                    comm_msg_info = msg['comm_msg_info']  # 该数据是本次推送多篇文章公共的
                    msg_id = comm_msg_info['id']  # 文章id
                    title=msg['app_msg_ext_info']['title']
                    url=msg['app_msg_ext_info']['content_url']
                    digest=msg['app_msg_ext_info']['digest']
                    msg_time = comm_msg_info['datetime']
                    #c_time = time.strftime("%Y_%m_%d_%H_%M_%S",msg_time)
                    c_time=datetime.datetime.fromtimestamp(int(msg_time))  #处理时间
                    print(msg_id,title,url,c_time)
                    #
                    # db = pymysql.connect(host='localhost', user='root', password='123456', port=3306,
                    #                      db='spiders')  # 创建数据库连接对象
                    # cursor = db.cursor()  # 获取mysql操作游标
                    # sql = 'INSERT INTO wx_title(id,digest,url,title,ctime) values(%s,%s,%s,%s,%s)'
                    # try:
                    #     cursor.execute(sql, (msg_id, digest, url, title,c_time))
                    #     db.commit()
                    # except:
                    #     db.rollback()
                    #     print('数据保存失败！！！')
                    # db.close()




                    #post_time = datetime.fromtimestamp(comm_msg_info['datetime'])  # 发布时间
                    # msg_type = comm_msg_info['type']  # 文章类型
                    # msg_data = json.dumps(comm_msg_info, ensure_ascii=False)  # msg原数据

             #       app_msg_ext_info = msg.get('app_msg_ext_info')  # article原数据
            #         if app_msg_ext_info:
            #             # 本次推送的首条文章
            #
            #             # 本次推送的其余文章
            #             multi_app_msg_item_list = app_msg_ext_info.get('multi_app_msg_item_list')
            #             if multi_app_msg_item_list:
            #                 for item in multi_app_msg_item_list:
            #                     msg_id = item['fileid']  # 文章id
            #                     if msg_id == 0:
            #                         msg_id = int(time.time() * 1000)  # 设置唯一id,解决部分文章id=0出现唯一索引冲突的情况
            #
            #     print('next offset is %d' % offset)
            # else:
            #     print('Before break , Current offset is %d' % offset)
            #     break
            #


if __name__ == '__main__':
    biz = 'MzIwOTcyNjI0Nw=='  # "菜鸟教程"
    pass_ticket = 'A5Fr9JF7Dt2l1rtta62NCUMScelNWDZ35K1poJCKYbZ0AXTNBZ1X1Zspr8PgwoXg'
    app_msg_token = '999_JZF6zxn9Qw30ffKsjcfjKyN5LNUy1Lh2xbSuBg~~'
    cookie ='wap_sid2=CIbuhucGElxiR1FQUzBYdERhV0laa0NRbHp0MXFtdFFrYlJOaHM4TlE1a3FBWEJ6eEJIMDVhZ3B2OXpsM09tbkwzS0VXVllmbTF5ZjJuUFJuTWZaelA4THhRUjJBdWNEQUFBfjD0wJzkBTgNQJVO'
    # 以上信息不同公众号每次抓取都需要借助抓包工具做修改
    wxMps = WxMps(biz, pass_ticket, app_msg_token, cookie)
    wxMps.start()  # 开始爬取文章
