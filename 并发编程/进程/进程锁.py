from multiprocessing import Process
from multiprocessing import Lock
import json
import time

def check():
    time.sleep(1)
    with open('tickect') as f:

        dic=json.load(f)
        print('余票%s张'%dic['tickect'])

def buy_tick(i,lock):
    #time.sleep(1)
    lock.acquire()
    with open('tickect') as f:

        dic=json.load(f)
        time.sleep(0.1)
    if dic['tickect']>0:
        dic['tickect']-=1
        print('买到票了')
    else:
        print('%d没买到票'%i)
    time.sleep(0.1)
    with open('tickect','w') as f:
         json.dump(dic,f)
    lock.release()
if __name__=='__main__':
    # for i in range(5):
    #     p=Process(target=check)
    #     p.start()
    lock=Lock()


    for i in range(5):
        p=Process(target=buy_tick,args=(i,lock))
        p.start()
