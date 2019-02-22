from multiprocessing import Process
import time


def func1():
    print("func1")
    time.sleep(10)
    print('func1结束')


def func2():
    print("func2")
    time.sleep(5)
    print("func2结束")


if __name__ == "__main__":
    p = Process(target=func1)
    p.daemon = True  # 守护线程
    p.start()
    func2()