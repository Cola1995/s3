from socket import *
import os
import struct
import json
import sys
ip_port=('127.0.0.1', 8083)
tcp_client=socket(AF_INET, SOCK_STREAM)
tcp_client.connect(ip_port)
user_list=[
    {'name':'alex','passwd':'123'},
    {'name':'linhaifeng','passwd':'123'},
    {'name':'wupeiqi','passwd':'123'},
    {'name':'yuanhao','passwd':'123'},
]

def Send():
    file_use = Check_user()
    if file_use==None:
        return ''
    while True:

        msg=input("输入要发送的文件路径--->").strip()

        file_size=os.path.getsize(msg)   #获取文件字节大小
        file_name=msg
        file_dict={                      #将文件信息封装到字典中
            'file_name':file_name,
            'file_size':file_size,
            'file_user':file_use
        }
        s_file_dict=json.dumps(file_dict)  #转换为字符转
        struct_file_dict=struct.pack('i',len(s_file_dict))

        tcp_client.send(struct_file_dict)

        tcp_client.send(s_file_dict.encode('utf-8'))
        with open(msg,'rb') as f:
            data=f.read()
        tcp_client.sendall(data)
    return '数据发送成功'
def Check_user():

    for i in range(len(user_list)):
        #print(user_list[i]['name'],user_list[i]['name'])
        if sys.argv[2]==user_list[i]['name'] and sys.argv[4]==user_list[i]['passwd']:
            print('loging successful')
            return r'C:\Users\Administrator\PycharmProjects\s3\网络编程\{0}'.format(user_list[i]['name'])
        # else:
        #     print('无效的用户名或密码')
            #break
            #return None
    print('无效的用户名或密码')





if __name__=='__main__':
    #Check_user()
    Send()
