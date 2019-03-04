from multiprocessing import Process
import time
def test(a1,a2):
    print("*"*a1)
    #time.sleep(5)
    print("="*a2)

if __name__=='__main__':

    # p=Process(target=test,args=(10,20))
    # p.start()
    # p.join() #等待子进程的结束，将异步程序改为同步
    # print('++++++:运行完了')
    p_list=[]
    for i in range(10):  #创建10个进程
        p = Process(target=test, args=(10*i, 20*i))
        #p_list.append(p)
        p.start()
        p_list.append(p)
        #p.join()
    #[p.join() for p in p_list] #列表推导式for p in p_list:p.join()
    for p in p_list:
        p.join()
    print('++++++:运行完了')
