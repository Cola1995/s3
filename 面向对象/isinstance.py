class Foo:
    pass

class T(Foo):
    pass


f=Foo()

print(isinstance(f,Foo))  #检查f是否是否是类 Foo 的对象
print(issubclass(T,Foo))   #检查sub类是否是 super 类的派生类