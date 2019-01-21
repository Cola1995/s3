import subprocess

from socket import *
# res = subprocess.Popen('dirs',
# #                                shell=True,
# #                                stderr=subprocess.PIPE,
# #                                stdout=subprocess.PIPE)
# # print(res.stdout.read().decode('GBK'))
# # print(res.stderr.read().decode('GBK'))
ip_port=('127.0.0.1',8082)
cmd_tcp_client=socket(AF_INET,SOCK_STREAM)
cmd_tcp_client.connect(ip_port)
while True:
    cmd=input("---->")
    if len(cmd)==0: continue
    if cmd=='quit': break
    cmd_tcp_client.send(cmd.encode('utf-8'))

    recive=cmd_tcp_client.recv(1024)
    print('客服端收到的消息是%s'%recive.decode('GBK'))


