from socket import *

sk=socket()
sk.connect(("127.0.0.1",8091))


while True:
    msg=input('___>:')
    sk.send(msg.encode('utf8'))
    data=sk.recv(1024).decode('utf8')
    print('客户端收到的消息是：',data)
sk.close()



