from multiprocessing import Process

class MyProcess(Process):
    def __init__(self,a,b):
        super().__init__()   #调用父类初始化方法
        self.a=a
        self.b=b

    def run(self):
        print(self.pid)
        print(self.name)
        print(self.a)
        print(self.b)



if __name__=='__main__':

    p1=MyProcess(1,2)
    p1.start()
    p2=MyProcess(8,9)
    p2.start()

    print('主进程')
    # 自定义类 继承Process类
    # 必须实现一个run方法,run方法中是在子进程中执行的代码