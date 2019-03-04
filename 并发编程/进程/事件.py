from multiprocessing import Event
#一个信号可以使所有的进程都进入阻塞状态
#也可以控制所有的进程接触阻塞
#一个事件被创建后。默认时阻塞状态
e=Event() #创建事件
print(e.is_set()) #查看时间的状态 默认False
print('111')
#e.set()  #将这个事件的状态改为True
e.wait() #依据e.is_set()的值决定是否阻塞
print('222')
#e.clear() #将事件的状态改为False