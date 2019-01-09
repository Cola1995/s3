class typed:

    def __init__(self,key):
        self.key=key

    def __get__(self, instance, owner):
        print('get方法')
        print(instance,owner)
        return instance.__dict__[self.key]

    def __set__(self, instance, value):
        print('set方法')
        print(instance,value)
        if instance is not str:
            raise TypeError('传入数据类型错误')
            #print('传入数据类型错误')
            return
        instance.__dict__[self.key]=value
        # print(instance.__dict__[self.key])
    def __delete__(self, instance):
        print('del方法')
        instance.__dict__.pop(self.key)




class aa:
    name=typed('name')
    def __init__(self,name,age):
        self.name=name
        self.age=age

a1=aa(12,10)
#del a1.name
print(a1.__dict__)





