import pymysql
import random

conn=pymysql.connect(host="localhost",database="db3",user="root",password="123456")



cursor=conn.cursor()

for i in range(100000):
    gen=str(random.randint(0,1))
    name="ma"+str(i)
    email="9{0}qq.com".format(i)
    sql="insert into san (name,email,gender) values ('{0}','{1}',{2})".format(name,email,gen)
    #print(sql)
    #
    #
    cursor.execute(sql)
    conn.commit()
    print("插入第%s条数据"%i)





cursor.close()
conn.close()