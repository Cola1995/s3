class ver1:
    def __init__(self,name,load,speed):
        self.name=name
        self.load=load
        self.speed=speed
    def run(self):
        print("开动了")



class subay(ver1):
    def __init__(self,name,load,speed,line):
        # ver .__init__(self,name,load,speed)
        super().__init__(name,load,speed)
        self.line=line

    def show(self):
        print(self.name,self.load,self.speed,self.line)

s1=subay('北京地铁',1000,"20km/H",'13号线')
s1.show()