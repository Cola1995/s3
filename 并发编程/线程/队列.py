#队列  先进先出
import queue

# q=queue.Queue
# q.put() #队列放置满阻塞
# q.put_nowait()  #队列放置满报错
# q.get()
# q.get_nowait()

#栈 先进后出
# q=queue.LifoQueue()
# q.put(1)
# q.put(2)
# q.put(3)
# print(q.get())

#优先级队列
q=queue.PriorityQueue()
q.put((20,"a"))
q.put((10,"b"))
q.put((30,"c"))

print(q.get())