a='slkfma'
import re

#print(a.find("ma"))
lijing='C:/Users/Administrator/PycharmProjects/s3/'
a1='2112a\l'
f=re.findall("a\\\\l",a1)
print(f)

f1=re.findall(r'a\\l',a1)
print(f1)
ff='abcabc'
fi=re.findall('(abc)*',ff)
print(fi)
s='abcmma132'
print(re.search('\d+',s))      #search查找的是结果是对象，通过group方法获取查找的值
print(re.search('\d+',s).group())
print(re.findall('[a-z]+',s))
gro='wang25ma24'    #分组查找
gf=re.search('(?P<name>[a-z]+)(?P<age>\d+)',gro).group('name')
print(gf)
fen='hell world|good'
fenf=re.split(r'[ |]',fen)    #以[ |]分割
print(fenf)

subb='aasd12aa89'    #字符串替换成其他字符
sss=re.sub('\d+','shu',subb)
print(sss)

ma='aca'
maf=re.match('a',ma).group()
print(maf)