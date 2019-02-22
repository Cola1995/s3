from concurrent.futures import ThreadPoolExecutor
import time

def func(n):
    time.sleep(2)
    print(n)
    return n*n

def call_back(m):
    print('回调结果是%s'%m.result())


tpool=ThreadPoolExecutor(max_workers=5)  #最大cpu数 *5


for i in range(20):
    t=tpool.submit(func,i).add_done_callback(call_back)


#
# tpool=ThreadPoolExecutor(max_workers=5)  #最大cpu数 *5
# t_list=[]
# #tpool.map(func,range(20)) #拿不到返回值
# for i in range(20):
#     t=tpool.submit(func,i)  #提交任务
#     t_list.append(t)
# #tpool.shutdown()  #close join
# print("主线程")
#
# for t in t_list:print("结果",t.result())