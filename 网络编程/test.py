import subprocess
import os
import struct
import json
# res = subprocess.Popen("dir",
#                                    shell=True,
#                                    stderr=subprocess.PIPE,
#                                    stdout=subprocess.PIPE)
# print(res.stdout.read())

s=os.path.getsize(r'C:\Users\Administrator\Desktop\ma.jpg')
# print(s)
# st=struct.pack('i',178240)
# print(len(st))
# print(type(178240))
file_dict={
        'filename':r'newC:\Users\Administrator\Desktop\ma.jpg',
        'file_size':2,
    }

# q=struct.pack('i',len(file_dict))
# print(type(q))
# ust=struct.unpack('i',q)
# print(ust)
#
# j_f=json.dumps(file_dict)
#
# print(type(j_f))
#
# b=j_f.encode('utf-8')
# print(type(b))
# jie=json.loads(j_f)
# print(jie)

# f=open(r'newC:\Users\Administrator\Desktop\ma.jpg', 'wb')
# f.write('s')
import re
wenjian=r'newC:\Users\Administrator\Desktop\ma\k.txt'

# r=re.findall('\\\.+[\s]',wenjian)
# fi=re.findall('[^<>/\\\|:""\*\?]+\.\w+$',wenjian) #匹配文件的正则
# print(fi)
# print(fi)
# l=[]
# for i in range(len(wenjian)):
#     #print(i)
#     if wenjian[i]=='\\':
#         print(wenjian[i])
#         l.append(i)
# print(l)
# print(wenjian[l[-1]+1:])
# path1=r'C:\Users\Administrator\PycharmProjects\s3\网络编程\file\qq'
# import sys
# print(sys.argv)


f=open('a.txt','rb')
for i in f.read():
    print(type(i))