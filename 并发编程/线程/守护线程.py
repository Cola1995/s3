# from threading import Thread
# import time
# def func1():
#     print('func1')
#     time.sleep(5)
# def func2():
#     print("func2")
#     time.sleep(10)
#
# t=Thread(target=func1)
# t.daemon=True    #守护线程
# t.start()
# t1=Thread(target=func2)
# t1.start()
# print("主进程")
#守护进程随着主进程代码的结束而结束
#守护线程接受后等待其他子线程的结束而结束

from multiprocessing import Process
import time
def func1():
    print("func1")
    time.sleep(5)
def func2():
    print("func2")
    time.sleep(10)
if __name__=="__main__":

    p=Process(target=func1)
    p.daemon=True    #守护线程
    p.start()

    print("主进程")