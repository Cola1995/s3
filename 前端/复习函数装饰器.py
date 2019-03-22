def wapper1(func):

    print("函数执行前")
    def aa(*args,**kwargs):
        # print("aaaaa")
        res=func(*args,**kwargs)
        return res


    return aa






@wapper1
def test(name,age):
    print("我是函数")
    return "函数返回值是%s,%s"%(name,age)

if __name__=="__main__":
    print(test("ma",24))

# def outer():
#     x = 1
#     y = 2
#
#     def inner():
#         print("x= %s" %x)
#         print("y= %s" %y)
#
#     print(inner.__closure__)
#     return inner
#
# outer()