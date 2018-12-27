class person:
    '人类'
    n='ma'
    a='a'
    def __init__(self,name,age,sex):

        self.name=name
        self.age=age
        self.sex=sex
    def eat(self):
        print('%s正在吃饭'%self.n)

    def play(self):
        print('玩')
p1=person('wang',20,'f')
# p1.eat()
# p2=person('ma',30,'f')
# p1.play()
print(p1.n)
del person.n
print(person.__dict__)

