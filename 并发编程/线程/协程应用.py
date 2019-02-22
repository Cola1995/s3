#协程：能够在一个线程中实现并发效果的概念
   #能够规避一些任务中的IO操作
   #在任务中的执行过程中，检测到IO就切换其他任务

#爬虫的例子
from gevent import monkey;monkey.patch_all()
import requests

import gevent
from urllib.request import urlopen
def get_url(url):
    response=urlopen(url)
    content=response.read().decode("utf-8")
    return len(content)



g1=gevent.spawn(get_url,"http://www.baidu.com")
g2=gevent.spawn(get_url,"http://www.sogou.com")
g3=gevent.spawn(get_url,"http://www.taobao.com")
g4=gevent.spawn(get_url,"http://www.cnblogs.com")
gevent.joinall([g1,g2,g3,g4])

print(g1.value)
print(g2.value)
print(g3.value)
print(g4.value)