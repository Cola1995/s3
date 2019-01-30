from multiprocessing import Queue,Process

# q=Queue(4)
# q.put(1)
# q.put(2)
# q.put(3)
# q.put(4)
#
# print(q.full())
#
# print(q.get())
# print(q.get())
# print(q.get())
# print(q.get())
# print(q.empty())
# try:
#     print(q.get_nowait())
# except:
#     print('队列已空')



def put(q):
    q.put('hello')

def get(q):
    print(q.get())

if __name__=='__main__':
    q=Queue()
    p1=Process(target=put,args=(q,))
    p1.start()
    p2=Process(target=get,args=(q,))
    p2.start()