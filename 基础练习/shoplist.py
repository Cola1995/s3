f=open('yonghu.txt','r',encoding='utf-8')
data=f.read()
print(data)
list=data.split('|')
dict1={'1011':{'name':"牛奶",'price':10},'1012':{'name':"蛋糕",'price':20}}
s=True
index=0
shopcar=[]
while s:
    username=input('请输入用户名：')
    if username=='q':
        s=False
        print(shopcar[0])
        continue
    password=input('请输入密码：')
    # print(username+password)
    # print(f"{list[0]}{list[1]}")
    if username+password==f"{list[0]}{list[1]}":
        print('登陆成功')
        gongzi=int(input('请输入你的工资：'))
        print(dict1)
        buy=input('请输入id:')
        shopcar.append(dict1[buy])
        if gongzi>shopcar[0]['price']:

            yue=gongzi-shopcar[0]['price']
            f1=open('yonghuinfo.txt','a',encoding='utf-8')

            f1.write('您购买的产品是：%s,价格：%d,剩余：%d\n'%(shopcar[0]['name'],shopcar[0]['price'],yue))
            f1.close()
            print('购买成功，剩余%d'%yue)
        else:
            print('穷鬼啥都买不起')
        #print(shopcar)
        break
    elif username+password!=f"{list[0]}{list[1]}":
        print('账号或密码错误')
        index+=1
        if index==3:
            s=False
            break



