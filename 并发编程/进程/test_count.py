def count():
    i=0
    z=0
    f=0
    list=[]
    while True:
        i+=1
        s=input("请输入整数")
        list.append(int(s))
        if i==10:break
    for a in list:
        if a>0:
            z+=1
        else:
            f+=1

    return z,f
print("正数的个数是%s，负数的个数是%s"%(count()[0],count()[1]))

