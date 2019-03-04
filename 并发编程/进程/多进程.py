from multiprocessing import Process
import time
import os
def test(args,args2):
    print(type(args),args,args2)
    time.sleep(3)
    print('%s我是子进程%s'%(time.strftime("%Y-%m-%d %X",time.localtime()),os.getpid()))
    print('子进程的父进程',os.getppid())

if __name__=="__main__":

    p=Process(target=test,args=('参数','参数2')) #注册
    p.start() #开启一个子进程
    print('%s我是父进程%s'%(time.strftime("%Y-%m-%d %X",time.localtime()),os.getpid()))  #查看进程号
    print('父进程的父进程',os.getppid()) #查看当前进程的父进程
    # input('sss')

