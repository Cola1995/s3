


# str1='s'
# li=[1,2,4,5,['a','b','c'],True]
# for itme in li:
#     #print(type(itme))
#     #print(itme)
#     if type(itme)==list:
#         #print('ok')
#         for i in itme:
#
#             print(i)
#     else:
#         print(itme)

p='p %.1f%%' %99.16112
print(p)
pp='name \033[45;1m%(name)+60s\033[0m age %(age)d' %{'name':'ma','age':18}
print(pp)
tpl = "numbers: {num:b},{num:o},{num:d},{num:x},{num:X}, {num:%}".format(num=15)
print(tpl)
def test(x):
    '''

    :param x:
    :return:
    '''
    y=x**2
    return y

print(test(4))
