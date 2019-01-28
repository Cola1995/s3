# 进程 与 进程之间
import os
from multiprocessing import Process

def func():
    global n   # 声明了一个全局变量
    n = 0       # 重新定义了一个n
    print('pid : %s'%os.getpid(),n)

if __name__ == '__main__':
    n = 100
    p = Process(target=func)
    p.start()
    p.join()
    print(os.getpid(),n)
