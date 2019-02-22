from threading import Thread,Semaphore
import time
def add(sm,a,b):
    sm.acquire()
    time.sleep(1)
    print(a+b)
    sm.release()



sm=Semaphore(3)


for i in range(10):
    Thread(target=add,args=(sm,i,i+3)).start()