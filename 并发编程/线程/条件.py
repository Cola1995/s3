# 条件
from threading import Condition

# 条件
# 锁
# acquire release
# 一个条件被创建之初 默认有一个False状态
# False状态 会影响wait一直处于等待状态
# notify(int数据类型)  造钥匙
from threading import Thread,Condition
def func(con,i):
    con.acquire()
    con.wait() # 等钥匙
    print('在第%s个循环里'%i)
    con.release()
con = Condition()
for i in range(10):
    Thread(target=func,args = (con,i)).start()
while True:
    num = int(input('>>>'))
    con.acquire()
    con.notify(num)  # 造钥匙
    con.release()

