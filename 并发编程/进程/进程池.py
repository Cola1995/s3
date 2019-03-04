from multiprocessing import Pool
import time
import os
def test(n):

    print('start%s'%n,os.getpid())
    time.sleep(1)
    print('end%s'%n,os.getpid())


if __name__=="__main__":
    p=Pool(5)
    for i in range(10):
        p.apply_async(test,args=(i,)) #异步调用
    p.close() #结束进程池接受任务
    p.join()  #感知进程池中的任务执行结束
