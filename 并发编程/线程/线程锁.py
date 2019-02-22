import time
from threading import Lock,Thread
# Lock 互斥锁
# def func(lock):
#     global n
#     lock.acquire()
#     temp = n
#     time.sleep(0.2)
#     n = temp - 1
#     lock.release()
#
# n = 10
# t_lst = []
# lock = Lock()
# for i in range(10):
#     t = Thread(target=func,args=(lock,))
#     t.start()
#     t_lst.append(t)

# for t in  t_lst: t.join()
# print(n)

# 科学家吃面

# noodle_lock  = Lock()
# fork_lock = Lock()
# def eat1(name):
#     noodle_lock.acquire()
#     print('%s拿到面条啦'%name)
#     fork_lock.acquire()
#     print('%s拿到叉子了'%name)
#     print('%s吃面'%name)
#     fork_lock.release()
#     noodle_lock.release()
#
# def eat2(name):
#     fork_lock.acquire()
#     print('%s拿到叉子了'%name)
#     time.sleep(1)
#     noodle_lock.acquire()
#     print('%s拿到面条啦'%name)
#     print('%s吃面'%name)
#     noodle_lock.release()
#     fork_lock.release()
#
# Thread(target=eat1,args=('alex',)).start()
# Thread(target=eat2,args=('Egon',)).start()
# Thread(target=eat1,args=('bossjin',)).start()
# Thread(target=eat2,args=('nezha',)).start()

from threading import RLock   # 递归锁
fork_lock = noodle_lock  = RLock()   # 一个钥匙串上的两把钥匙
def eat1(name):
    noodle_lock.acquire()            # 一把钥匙
    print('%s拿到面条啦'%name)
    fork_lock.acquire()
    print('%s拿到叉子了'%name)
    print('%s吃面'%name)
    fork_lock.release()
    noodle_lock.release()

def eat2(name):
    fork_lock.acquire()
    print('%s拿到叉子了'%name)
    time.sleep(1)
    noodle_lock.acquire()
    print('%s拿到面条啦'%name)
    print('%s吃面'%name)
    noodle_lock.release()
    fork_lock.release()

Thread(target=eat1,args=('alex',)).start()
Thread(target=eat2,args=('Egon',)).start()
Thread(target=eat1,args=('bossjin',)).start()
Thread(target=eat2,args=('nezha',)).start()