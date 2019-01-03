class People:
    __star="earth"
    def __init__(self,name,age,sex):
        # print(self.star)
        self.name=name
        self.age=age
        self.sex=sex


    def show(self):
        print("我是%s人"%self.name)


p=People('ma',12,'nan')
print(p._People__star)
print(People.__dict__)
