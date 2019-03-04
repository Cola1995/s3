import time
from multiprocessing import Process

def func(a,b):

    while True:
        time.sleep(0.2)
        print('我是子进程我还活着',time.strftime('%Y-%m-%d %X',time.localtime()))


def func1():
    i = 0
    while i < 3:
        i += 1
        time.sleep(1)
        print('我是子进程1',time.strftime('%Y-%m-%d %X',time.localtime()))


if __name__=="__main__":
    #p=Process(target=func,args=(1,2))
    #p.daemon=True   #守护进程
    #p.start()

    #
    p1=Process(target=func1)
    p1.start()
    p1.terminate() #在主进程内结束一个子进程
    #print('我是主进程', time.strftime('%Y-%m-%d %X', time.localtime()))

    i=0
    while i<5:
        i+=1
        time.sleep(1)
        print('我是主进程')
        print(p1.is_alive()) #检测一个进程是否活着


    #守护进程会随着主进程代码执行完毕尔结束
    #结束进程不是马上生效，需要操作系统响应的过程
    #p.name 名字  p.pid 进程号