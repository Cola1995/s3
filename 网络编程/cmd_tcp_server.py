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
        try:
            data=conn.recv(buffer_size)
            print('服务端收到的消息是%s'%data.decode('utf-8'))
            if len(data)==0:break
            res = subprocess.Popen(data.decode('utf-8'),
                                   shell=True,
                                   stderr=subprocess.PIPE,
                                   stdout=subprocess.PIPE)

            err=res.stderr.read()
            if err:
                cmd_res=err
            else:
                cmd_res=res.stdout.read()
            conn.send(cmd_res)
        except Exception as e:
            print(e)
            break




    conn.close()


cmd_tcp_server.close()