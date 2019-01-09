text=" helloworldkk \n"
text1="nvhvhvivj"
print(text[:-1])  #字符串切片[1:6] 1<=x<6
for i in range(len(text)):   #循环字符串每个字符
    print(text[i])
print(text)
print(text.strip())  #去除左右空格及\n
print(text.lstrip()) #去除左空格
print(text.rstrip()) #去除右空格
print(text1.split('v'))  #以特定字符区分字符串，结果是列表
print(text1.upper())  #转大写
print(text1.lower()) #转小写
print(text1.startswith('n'))  #判断字符串以某字符串开头返回boolean值
print(text1.endswith('j'))     #判断字符串以某字符串结尾返回boolean值
name='ma'
age='23'
sex='nan'
t="姓名：{0}年龄：{1} 性别{2}："
t1="姓名：{name}年龄：{age} 性别{sex}："

print(t.format("ma",12,"nan"))
print(t.format(name,age,sex))
tag=','
str_tag=tag.join(text1)
print(str_tag)

list_tag=list(str_tag) #字符串转列表
s=str(list_tag)
print(s,type(s))
#dict_tag=dict(str_tag)
print(list_tag,type(list_tag))
sso="12"
print(sso.isdigit())  #判断字符是否为数字
#更多方法详见http://www.cnblogs.com/linhaifeng/articles/7133357.html