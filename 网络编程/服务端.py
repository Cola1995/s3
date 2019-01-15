
from socket import *

ip_port=('127.0.0.1',8091)
back_log=5
buff_size=1024
tcp_server=socket(AF_INET,SOCK_STREAM)
tcp_server.bind(ip_port)    #设置ip端口号
tcp_server.listen(back_log)
while True:
    conn,addr=tcp_server.accept()  #等待连接
    while True:
        try:
            msg=conn.recv(buff_size)   #服务端接受消息
        except Exception:
            break
        print('客户端发来的消息是',msg.decode('utf-8'))

        conn.send(msg.upper())     #服务端回复消息
    conn.close()
tcp_server.close()