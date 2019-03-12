class seller:
    pre='1000'
    def __init__(self,name,addr):
        self.name=name
        self.addr=addr


    def sell_house(self):
        print('%s 正在卖房子'%self.name)


s1=seller('链家','天龙苑')

print(getattr(s1,'sell_house1','ok1')) #获取属性值,不存在则报错，如果存在默认值，返回默认值

print(hasattr(s1,'pre'))  #判断s1.属性是否存在，返回bool值
# print(s1.__dict__)
# setattr(s1,'sb','True')   #设置属性
# print(s1.__dict__)
# delattr(s1,"sb")    #删除属性值
# print(s1.__dict__)
#
# setattr(s1,'func',lambda x:x.name+'sb')
# print(s1.__dict__)
# print(s1.func(s1))