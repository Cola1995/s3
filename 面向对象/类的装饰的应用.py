class typed:  #描述符

    def __init__(self,key,type):
        self.key=key
        self.type=type

    def __get__(self, instance, owner):
        print('get方法')
        print(instance,owner)
        return instance.__dict__[self.key]

    def __set__(self, instance, value):
        print('set方法')
        print(type(instance),type(value),self.type)
        if type(value) is not self.type:
        # if not isinstance(value, self.type):
            raise TypeError('传入数据类型错误,%s传入类型应为%s'%(self.key,self.type))
            #print('传入数据类型错误')
            #return
        instance.__dict__[self.key]=value
        # print(instance.__dict__[self.key])
    def __delete__(self, instance):
        print('del方法')
        instance.__dict__.pop(self.key)


def deco(**kwargs):    #装饰器
    def wap(obj):
        # obj.x=1
        # obj.y=2
        # obj.z=3
        # print(kwargs, obj)
        for key,val in kwargs.items(): #循环字典
            setattr(obj,key,typed(key,val))   #设置属性

        return obj

    return wap

@deco(name=str,age=int,gongzi=float)
class aa:
    #name=typed('name',str)
    def __init__(self,name,age,gongzi):
        self.name=name
        self.age=age
        self.gongzi=gongzi

a1=aa('oo',2,12.0)
#del a1.name
print(aa.__dict__)
print(a1.__dict__)




