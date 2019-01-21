import socketserver
import struct
import json
import time
import sys
class MyServer(socketserver.BaseRequestHandler):
    def handle(self):
        # print('conn is ',self.request)  #conn
        # print('addr is ',self.client_address) #addr


        while True:
            try:
                #收消息
                data=self.request.recv(4)
                #if not data:break
                #print('收到客户端的消息是',data)
                len_file_dict=struct.unpack('i',data)[0]

                data2=self.request.recv(len_file_dict)
                #print(type(data2),data2)
                dict=json.loads(data2.decode('utf-8'))
                #print(dict['file_name'])
                filesize_b=dict['file_size']
                r_b=b''
                recv_len=0
                buffsize=1024
                f_list = []
                for i in range(len(dict['file_name'])):   #处理接受的文件名
                    # print(i)
                    if dict['file_name'][i] == '\\':
                        #print(dict['file_name'])
                        f_list.append(i)

                print(dict['file_name'][f_list[-1] + 1:])
                filename=dict['file_name'][f_list[-1] + 1:]

                path1 = dict['file_user']  #写文件的路径
                f_path=path1+r'\\'+filename
                f1 = open(f_path,'wb')
                while recv_len<  dict['file_size']:  #每次只接受1024字节的数据，判断最后一次接受多少数据
                    if dict['file_size']-recv_len>buffsize:
                        buffsize=1024
                    else:
                        buffsize=dict['file_size']-recv_len

                    file_data = self.request.recv(buffsize)
                    recv_len+=buffsize
                    # print(recv_len,dict['file_size'])
                    # print(file_data)
                    #r_b+=file_data
                    f1.write(file_data)
                    sys.stdout.write("\r# Process: %0.1f%%" % (float(recv_len) / float(dict['file_size']) * 100))  #进度条
                    time.sleep(0.1)
                    sys.stdout.flush()  # 刷新缓存
                print('数据写入成功')

                f1.close()
                #发消息
                #self.request.sendall(data.upper())
            except Exception:
                break


if __name__=='__main__':
    s=socketserver.ThreadingTCPServer(('127.0.0.1',8083),MyServer)
    s.serve_forever()