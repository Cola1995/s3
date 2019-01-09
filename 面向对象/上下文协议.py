class Foo:

    def __enter__(self):

        print('__enter__')
        return self


    def __exit__(self, exc_type, exc_val, exc_tb):
        print("exit")

#f=Foo()
with Foo() as f: #with obj 触发obj.__enter__方法拿到返回值，执行代码块，没有异常的情况下，整个代码块运行完毕后去触发--exit————2.有异常的情况下，从异常出现的位置直接触发——exit-—a.如果返回TRUE 代表吞掉异常b.如果的返回值不为TRUE代表吐出异常C.exit的运行完毕代表整个with语句执行完毕
    print(f)