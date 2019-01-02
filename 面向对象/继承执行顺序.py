class A:
    def test(self):
        print('A')
class B(A):
    # def test(self):
    #     print('B')
    pass
class D(B):
    # def test(self):
    #     print('D')
    pass



class C(A):
    # def test(self):
    #     print("C")
    pass

class E(C):
    # def test(self):
    #     print("E")
    pass
class F(D,E):
    # def test(self):
    #     print("F")
    pass
f=F()
f.test()
print(F.__mro__)
