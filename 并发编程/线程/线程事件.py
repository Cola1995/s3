#事件被创建的时候
#False wait() 阻塞

#True wait()非阻塞

#clear（） 设置为false
#set 设置状态为True
#  数据库 - 文件夹
#  文件夹里有好多excel表格
    # 1.能够更方便的对数据进行增删改查
    # 2.安全访问的机制


#  起两个线程
#  第一个线程 : 连接数据库
        # 等待一个信号 告诉我我们之间的网络是通的
        # 连接数据库
#  第二个线程 : 检测与数据库之间的网络是否连通
        # time.sleep(0,2) 2
        # 将事件的状态设置为True
import time
import random
from threading import Thread,Event
def connect_db(e):
    count = 0
    while count < 3:
        e.wait(0.5)   # 状态为False的时候,我只等待1s就结束
        if e.is_set() == True:
            print('连接数据库')
            break
        else:
            count += 1
            print('第%s次连接失败'%count)
    else:
        raise TimeoutError('数据库连接超时')

def check_web(e):
    time.sleep(random.randint(0,3))
    e.set()

e = Event()
t1 = Thread(target=connect_db,args=(e,))
t2 = Thread(target=check_web,args=(e,))
t1.start()
t2.start()



