from socket import *
ip_port=('127.0.0.1',8080)
buffer_size=1024

udp_server=socket(AF_INET,SOCK_DGRAM) #数据报
udp_server.bind(ip_port)

while True:
    data,addr=udp_server.recvfrom(buffer_size)  #以元组的方式接收客户端消息（字节）
    print(addr,data.decode('utf-8'))

    udp_server.sendto(data.upper(),addr)  #回复消息给相应客户端