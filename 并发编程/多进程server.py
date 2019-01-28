from socket import *
from multiprocessing import Process


def pr(conn):
    data = conn.recv(1024).decode('utf8')
    print("服务端收到的消息是:", data)
    conn.send('再见'.encode('utf8'))
    conn.close()



if __name__=="__main__":
    sk = socket()
    sk.bind(('127.0.0.1', 8091))
    sk.listen()
    while True:
        conn,addr = sk.accept()
        p = Process(target=pr,args=(conn,))
        p.start()
        #sk.close()
    #sk.close()