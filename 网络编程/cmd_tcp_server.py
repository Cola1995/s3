from socket import *
import subprocess
ip_port=('127.0.0.1',8082)
buffer_size=1024
listen=5

cmd_tcp_server=socket(AF_INET,SOCK_STREAM)

cmd_tcp_server.bind(ip_port)
cmd_tcp_server.listen(listen)

while True:
    conn,addr=cmd_tcp_server.accept()

    while True:

        data=conn.recv(buffer_size)
        print(data)
        if len(data)==0:break
        res = subprocess.Popen(data.decode('utf-8'),
                               shell=True,
                               stderr=subprocess.PIPE,
                               stdout=subprocess.PIPE)

        conn.send(res.stdout.read())




    conn.close()


cmd_tcp_server.close()