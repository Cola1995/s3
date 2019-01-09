import time

def a(type='a'):
    def wap(func):
        def show():
            if type=='a':
                start_time=time.time()
                time.sleep(2)
                res=func()
                end_time=time.time()
                print("函数的执行时间是%s"%(end_time-start_time))
                return res
            else:
                res=func()
                print('type的值是B')
                return res

        return show

    return wap






@a(type='a')
def test():
    print('test函数运行')
    return "这是test函数的返回值"
@a(type='b')
def test2():
    print('test2函数运行')
    return "这是test函数的返回值"


# test=wap(test)
# print(test())
print(test2())