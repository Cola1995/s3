class people:

    def __init__(self,name,age):
        self.name=name
        self.age=age

    def ded(self):
        del self.name



p1=people('ma',24)
print(p1.__dict__)
p1.ded()
print(p1.__dict__)