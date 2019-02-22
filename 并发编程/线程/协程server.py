from gevent import monkey;monkey.patch_all()
import socket
import gevent
sk=socket.socket()
sk.bind(('127.0.0.1',8089))
sk.listen()

def talk(conn):
    conn.send(b"hello")
    print(conn.recv(1024).decode("utf-8"))
    conn.close()


while True:
    conn,addr=sk.accept()
    gevent.spawn(talk,conn)


sk.close()