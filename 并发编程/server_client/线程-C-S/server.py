import socket
from threading import Thread
sk=socket.socket()
sk.bind(("127.0.0.1",8087))
sk.listen()
def chat(conn):
    while True:
        data=conn.recv(1024).decode('utf-8')
        print(data)
while True:
    conn,addr=sk.accept()
    Thread(target=chat,args=(conn,)).start()
conn.close()
sk.close()