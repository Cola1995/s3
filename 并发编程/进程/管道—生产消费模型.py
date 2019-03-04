from multiprocessing import Lock,Pipe,Process
import time
import random

def producer(name,food,cus,pro):
    cus.close()
    for i in range(2):
        time.sleep(random.random())
        f="%s生产了%s%s"%(name,food,i)
        print(f)
        pro.send(f)
    pro.close()
def customer(cus,pro,name):
    pro.close()
    while True:
        try:

            food=cus.recv()

            time.sleep(random.random())
            print("%s消费了%s"%(name,food))
        except EOFError:
            cus.close()

            break



if __name__=="__main__":
    cus,pro=Pipe()
    lock=Lock()


    p=Process(target=producer,args=('alex','面条',cus,pro))
    p.start()
    c=Process(target=customer,args=(cus,pro,"wusir"))
    c.start()
    c1= Process(target=customer, args=(cus, pro, "yuan"))
    c1.start()

    cus.close()
    pro.close()