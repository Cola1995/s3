from multiprocessing import JoinableQueue,Process
import time
import random

def prodecer(name,food,q):
    for i in range(2):
        time.sleep(random.randint(1,3))
        f='%s生产了%s%d'%(name,food,i)
        print(f)
        q.put(f)
    q.join()


def cusomer(name,q):

    while True:
        food=q.get()
        if food is None:break
        print("%s消费了%s"%(name,food))
        time.sleep(random.randint(1, 3))
        q.task_done()
if __name__=="__main__":
    q=JoinableQueue(20)

    p1=Process(target=prodecer,args=('alex','包子',q))
    p2=Process(target=prodecer,args=('Egon','馒头',q))
    c1=Process(target=cusomer,args=('wusir',q))
    c2=Process(target=cusomer,args=('lihaifeng',q))
    p1.start()
    p2.start()
    c1.daemon=True
    c2.daemon=True
    c1.start()
    c2.start()
    p1.join()
    p2.join()
