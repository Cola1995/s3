from socket import *
import os
import struct
import json
ip_port=('127.0.0.1', 8083)
tcp_client=socket(AF_INET, SOCK_STREAM)
tcp_client.connect(ip_port)


while True:
    msg=input("输入要发送的文件路径--->").strip()

    file_size=os.path.getsize(msg)   #获取文件字节大小
    file_name='new'+msg
    file_dict={                      #将文件信息封装到字典中
        'file_name':file_name,
        'file_size':file_size,
    }
    s_file_dict=json.dumps(file_dict)  #转换为字符转
    struct_file_dict=struct.pack('i',len(s_file_dict))

    tcp_client.send(struct_file_dict)

    tcp_client.send(s_file_dict.encode('utf-8'))
    with open(msg,'rb') as f:
        data=f.read()
    tcp_client.sendall(data)