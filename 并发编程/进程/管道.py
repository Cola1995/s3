from multiprocessing import Pipe,Process

def test(conn1,conn2):
    conn1.close()
    while True:
        try:
            msg=conn2.recv()
            print(msg)
        except EOFError:
            conn2.close()
            break



if __name__=="__main__":
    conn1,conn2=Pipe()

    Process(target=test,args=(conn1,conn2)).start()
    conn2.close()
    for i in range(5):
        conn1.send('你好%s'%i)
    conn1.close()


#pipe 数据不安全
#枷锁来控制管道的行为 来避免进程之间争抢数据造成数据不安全的现象


#队列相对管道是安全的
#队列是基于管道优化的