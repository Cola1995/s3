
import time
def timea(func):
    def wap(*args,**kwargs):

        stat_time=time.time()
        res=func(*args,**kwargs)

        stop_time=time.time()
        print('函数的运行时间是%s'%(stop_time-stat_time))
        return res

    return wap


@timea   # test=timea(test)
def test(name,age):
    time.sleep(3)
    print("函数运行完毕,姓名是%s 年龄是%d"%(name,age))
    return '这是test的返回值'

def test1(name,age,male):
    time.sleep(3)
    print("函数运行完毕,姓名是%s 年龄是%d,性别是%s"%(name,age,male))
    return '这是test1的返回值'

# test=timea(test)
print(test('mahongda',23))
#print(test1('mahongda',23,'nan'))
