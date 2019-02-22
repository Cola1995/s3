# from gevent import monkey;monkey.patch_all()
import gevent
import time


def eat():
    print("Star eating")
    gevent.sleep(1)
    print("end eating")

def play():
    print("start play")
    gevent.sleep(1)
    print("end play")



g1=gevent.spawn(eat)
g2=gevent.spawn(play)
g1.join()
g2.join()
#进程和线程的任务切换由操作系统完成
#协程任务之间的任务切换由（代码）完成，只有遇到协程模块能识别的IO操作的时候，程序才会进行切换，实现并发效果

#协程：能够在一个线程中实现并发



# def eat():
#     print("Star eating")
#     time.sleep(1)
#     print("end eating")
#
# def play():
#     print("start play")
#     time.sleep(1)
#     print("end play")
#
#
#
# g1=gevent.spawn(eat)
# g2=gevent.spawn(play)
# g1.join()
# g2.join()