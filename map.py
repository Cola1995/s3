#map函数
array=[1, 2, 3, 4]
num1=[1,2,3,4]
def add_one(x):
    return x+1
def pf(x):
    return x**2
def map_list(func,array):

    for i in range(len(array)):


        array[i]=func(array[i])
    return array
def map_add(arr):
    for i in range(len(arr)):
        arr[i]=arr[i]+1
    return arr

# t=map_list([1,2,3,4])
# a=map_add([1,2,3,4])
# t=map_list(pf,[1,2,3,4])
# a=map_list(lambda x:x-1,[1,2,3,4])
# print(t)
# print(a)
# t=map(lambda x:x+1,[1,2,3,4])
# print(list(t))

#map filter 函数
# fimally=['mayuli','mayuting','huoguifen']
# res=filter(lambda x:x.startswith('ma'),fimally)
# print(list(res))

#reduce 函数
from functools import reduce
np=[1,2,3,4]
print(reduce(lambda x,y:x*y,np,100))
print(all('0'))

#内置函数
name='你好'
print(bytes(name,encoding='utf-8')) #编码
print(bytes(name,encoding='utf-8').decode("utf-8"))  #解码

#ascll码
print(chr(97))
#打印某有个对象下有哪些方法
print(dir(all))

#10除三取余  (3, 1)
print(divmod(10,3))

#将字符串提取成字典,将字符串中表达式运算
str1="{'name':'alex'}"
a='1+2'
print(eval(str1))
print(eval(a))

ll=['a15','b10','c9']
print(list(max(ll)))
#max方法使用
b=[
    {'name':'ma','age':18},
    {'name':'wang','age':20}
]
print(max(b,key=lambda dic:dic['age']))

dic={'age1':18,'age2':10}
print(max(zip(dic.values(),dic.keys())))