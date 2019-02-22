from threading import Thread
import time

def watch(name):
    a=input("请输入")
    print("%s%s 正在看电视"%(time.time(),name))
def drink(name):
    print("%s%s 正在喝水"%(time.time(),name))

if __name__=="__main__":
    t=Thread(target=watch,args=("ma",))
    print(t.getName())
    t.start()
    t2=Thread(target=drink,args=('wang',))
    print(t2.getName())
    t2.start()
    #进程是最小的内存分配单元
    #线程是操作系统调度的最小单位
    #线程被cpu执行了
    #进程内至少包含了一个线程
    #进程中可以开启多个线程
      #开启一个线程所需要的时间远远小于开启一个进程
      #多个线程内部有自己的数据栈，数据不共享
      #全局变量在多线程之间是共享的
    #全局解释器锁 GIL
        #锁的是什么？线程
        #效率降低，只能一个线程在cpu中运行
        #python语言的问题吗？ 是Cpython解释器的特性
    #在Cpython解释器下的python程序在同一时刻多线程中只能有一个线程被cpu执行
    #高IO:爬取网页  多线程
         #QQ聊天
        #处理日志文件 读文件
        #读数据库
        #处理web请求
    #高CPU :计算类   多进程

