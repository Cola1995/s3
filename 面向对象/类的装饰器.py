
def typed(**kwargs):
    def deco(obj):
        # obj.x=1
        # obj.y=2
        # obj.z=3
        # print(kwargs, obj)
        for key,val in kwargs.items(): #循环字典
            setattr(obj,key,val)   #设置属性

        return obj

    return deco

@typed(x=1,y=2)
class Foo:
    # print('ok')
    pass
print(Foo.__dict__)

@typed(name="alex")
class bar:
    pass

print(bar.__dict__)