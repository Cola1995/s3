class Tel:
    tr=999
    def __init__(self,pinpai,xh,pr,c):
        self.pinpai=pinpai
        self.xh=xh
        self.pr=pr
        self.c=c
    def show(self):
        print("%s品牌的%s型号的手机的价格是%d"%(self.pinpai,self.xh,self.pr))
    @property     #静态属性
    def buy(self):
        return self.c*self.pr
    @classmethod      #类属性
    # def tt(self):
    #     print(self.tr)
    def tt(cls,q):
        print(cls.tr,q)


t1=Tel("oppo","r9s",2799,2)
#t1.show()
# print(t1.buy)     #调用时不要加括号
Tel.tt(2)
