

class Foo:
    def __init__(self,x):
        self.x=x

    def __getattr__(self, item):
        print('执行的是我')
        # return self.__dict__[item]
    def __getattribute__(self, item):
        print('不管是否存在,我都会执行')
        raise AttributeError('哈哈')

f1=Foo(10)
f1.x
f1.xxxxxx

#当__getattribute__与__getattr__同时存在,只会执行__getattrbute__,除非__getattribute__在执行过程中抛出异常AttributeError二者同时出现
#http://www.cnblogs.com/linhaifeng/articles/6204014.html