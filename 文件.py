f=open('a.py','rb') #读取文件内容 b的方式不能制定编码
# f.write('hai\n')
# f.write('nihoa')

# data=f.read()
#文件以bytes形式存在于硬盘上
#str----encode--->bytes
#bytes--->decode-->str
# print(data.decode('utf-8'))
# f.close()

#f=open('test1.py','wb')
#f.write(bytes('111',encoding='utf-8')) #编码
#f.write(('11').encode('utf-8'))#编码
# f=open('a.py','rb')
# data=f.readlines()
# print(data)
# f=open('a.py','a',encoding='utf-8')
# f.write('马宏达')

#读取文件最后一行
# f=open('a.py','rb')
# for i in f:         #循环文件的推荐方式
#     offs=-1
#     while True:
#         f.seek(offs,2)
#         data=f.readlines()
#         if len(data)>1:
#             print('文件的最后一行是%s'%(data[-1].decode(encoding='utf-8')))
#             break
#         offs*=2

# data=f.readlines()
# print(list(map(lambda x:x.decode('utf-8'),data)))
# print(len(data))

# data=f.read()
# print(data)
with open('user_list.txt','r') as read_f:
    for i in read_f:
        print(i.strip())

