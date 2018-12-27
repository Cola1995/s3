from test.cal import add
from test import cal
import time
# import sys
#print(add(1, 1))
# print(sys.path)
#时间戳
print(time.time()) #1544688721.9046378秒  从1970凌晨到现在多少秒


#结构化时间，当地时间
t=time.localtime(1412545454)
s='{0}:{1}:{2}:{3}'
ss=s.format(t.tm_year,t.tm_mon,t.tm_mday,t.tm_hour)
print(ss)
print(t)

#结构化时间 UTC
print(time.gmtime())

#将结构化时间转化成时间戳
print(time.mktime(time.localtime()))


#将结构化时间转化为字符串时间
# 2018-12-13 16:38:34
print(time.strftime("%Y-%m-%d %X",time.localtime()))

#将字符串时间转化为结构化时间
print(time.strptime("2018-12-13 16:38:34","%Y-%m-%d %X"))

#固定格式的时间
print(time.asctime())

print(time.ctime())


import datetime

print(datetime.datetime.now())