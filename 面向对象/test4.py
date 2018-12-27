class School:

    def __init__(self,name,addr,tel):
        self.name=name
        self.addr=addr
        self.tel=tel


    def  call(self):
        print('%s电话号码是%d'%(self.name,self.tel))

    def  fangjia(self):
        print('%s学校9号放假'%(self.name))




s1=School('oldboy','沙河地铁站',78956)
s1.call()
s1.fangjia()