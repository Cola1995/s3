class School:
    def __init__(self,name,addrs):
        self.name=name
        self.addrs=addrs
    def zhaosheng(self):
        print("正在招生")
s1=School("oldboy",'沙河地铁站会的上海市')
s2=School("创智博客","不知道在哪")


class Kechen:
    def __init__(self,name,z,pir,school):
        self.name=name
        self.z=z
        self.pir=pir
        self.school=school

    def shangke(self):
        print('正在上课')


# k1=Kechen('linux',20,3000,s1)
# k2=Kechen('python',20,5000,s2)


class Teacher:
    def __init__(self,name,xinshui,age,k):
        self.name=name
        self.xinshui=xinshui
        self.age=age
        self.k=k

    def jiang(self):

        print('正在上课')
# t1=Teacher('wupeiqi',10000,35)
# t2=Teacher("alex",20000,38)
msg_sch='''
1 oldboy  沙河地铁站会的上海市
2 创智博客 不知道在哪
'''
msg_k='''
1 linux   20 3000
2 python    20 5000 

'''
msg_t='''
1  wupeiqi 10000 35
2  alex    20000 38

'''
while True:
    print(msg_sch)
    men_s={
        "1":s1,
        "2":s2,
    }


    s_in=input('请输入要选择的学校————————》')
    print(msg_k)
    
    k1 = Kechen('linux', 20, 3000, men_s[s_in])
    k2 = Kechen('python',20,5000,men_s[s_in])
    men_k={
        '1':k1,
        '2':k2
    }
    k_in = input("请输入要选择的课程————————》")



    t1 = Teacher('wupeiqi', 10000, 35,men_k[k_in])
    t2 = Teacher("alex",20000,38,men_k[k_in])

    print(msg_t)
    t_in = input('"请输入要选择老师————————》"')
    if t_in =="1":
        print("您选择的学校是%s,课程%s,老师%s"%(t1.k.school.name,t1.k.name,t1.name))
    else:
        print("您选择的学校是%s,课程%s,老师%s" % (t2.k.school.name, t2.k.name, t2.name))

