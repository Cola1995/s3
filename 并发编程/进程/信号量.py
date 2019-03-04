from multiprocessing import Semaphore
import time
from multiprocessing import Process
# s=Semaphore(4)
# s.acquire()
# print('第一把钥匙')
# s.acquire()
# print('第二把钥匙')
# s.acquire()
# print('第三把钥匙')
# s.acquire()
# print('第四把钥匙')
# s.release()
# s.acquire()
#
# print('第五把钥匙')
def ktv(i,s):
    s.acquire()
    print('%d进去了'%i)
    time.sleep(3)
    print('%d出来了'%i)
    s.release()

if __name__=="__main__":
    s=Semaphore(3)
    for i in range(10):
        p=Process(target=ktv,args=(i,s))
        p.start()