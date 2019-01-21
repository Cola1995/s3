from socket import *

ip_port=('127.0.0.1', 8083)
tcp_client=socket(AF_INET, SOCK_STREAM)
tcp_client.connect(ip_port)


while True:
    msg=input("--->")
    tcp_client.send(msg.encode('utf-8'))  #客服端发送消息
    data=tcp_client.recv(1024)                #客户端接受消息
    print('收到服务端发送的消息',data.decode('utf-8'))
