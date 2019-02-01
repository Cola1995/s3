import socket
from multiprocessing import Pool

def talk(conn):
    conn.send(b'hello')
    data = conn.recv(1024).decode('utf-8')
    print(data)
    conn.close()

if __name__=="__main__":
    p=Pool(5)
    sk=socket.socket()
    sk.bind(("127.0.0.1",8087))
    sk.listen()

    while True:
        conn,addr=sk.accept()
        p.apply_async(talk,args=(conn,))
    sk.close()