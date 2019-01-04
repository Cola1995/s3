class Foo:
    def __set__(self, instance, value):
        print('set方法')
    def __get__(self, instance, owner):
        print('get方法')
    def __delete__(self, instance):
        print('delete方法')


class bar:
    x=Foo()
    def __init__(self):
        pass

b=bar()
b.x=1
del b.x
#http://www.cnblogs.com/linhaifeng/articles/6204014.html