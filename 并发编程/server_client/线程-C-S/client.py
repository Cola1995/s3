import socket

sk=socket.socket()
sk.connect(("127.0.0.1",8087))

while True:

    s=input("客户端输入").encode('utf-8')
    sk.send(s)
sk.close()