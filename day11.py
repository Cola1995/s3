# str='ssajkdsdssddd'
# str=input()
# print(str)
# a=str.zfill(10)
# b=str.rjust(10,'*')
# c = str.ljust(10, '*')
# print(a,b,c)
# s=str.split('s')
# print(s)
# c=str.find('a')
# print(c)

# for item in range(len(str)):
#     print(str[item],item)

# r=range(0,100)
# for i in r:
#     print(i)
name = 'alex'
t = name.startswith('al')
d = name.endswith('X')
r = name.replace('l', 'p')
s = name.split('l')
u = name.upper()
l = name.lower()
f = name.find('e')
j = '_'.join(name)
print(t, d, r, s, u, l, f, j)
# n1=input('1+++')
# # n2=input('2')
# # str='我是{0},年龄{1}'
# # print(str.format(n1,n2))
n3 = input('请输入你喜欢的片名：')
pp = n3.replace('苍井空', '***')
print(pp)
