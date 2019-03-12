class Foo:
    x=1
    def __init__(self,y):
        self.y=y

    def __getattr__(self, item):  #先查找实例属性，只有obj.属性不存在时触发
        print('查找的%s属性不存在'%item)

    def __delattr__(self, item): #删除属性时触发
        self.__dict__.pop(item)

    def __setattr__(self, key, value):  #设置属性值时触发
        print('—setattr--')
        self.__dict__[key]=value


    def play1(self):
        print("这是play放法")
f=Foo(10)
print(getattr(f,"play11","pk"))
# print(f.play1())
# print(f.r)
# print(f.__dict__)
# f.q=12
# print(f.__dict__)
# del f.q
# print(f.__dict__)




