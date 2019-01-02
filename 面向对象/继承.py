class Dad:
    money=160000
    def __init__(self,name):
        self.name=name
    def drink(self):
        print('%s正在喝酒'%self.name)



class Son(Dad):
    pass


print(Son.money)
