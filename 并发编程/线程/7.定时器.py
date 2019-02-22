import time
from threading import Timer
def func():
    print('时间同步')   #1-3

while True:
    t = Timer(5,func).start()   # 非阻塞的
    time.sleep(5)