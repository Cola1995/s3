import pymysql

conn=pymysql.connect(host="localhost",database="db3",user="root",password="123456")



cursor=conn.cursor()
# sql="insert into userinfo (username,password) values ('ma',123456)"
# cursor.execute(sql)
# conn.commit()

sql="select * from userinfo"
#cursor.execute(sql)
cursor.callproc('p3',(10,10))

cursor.callproc('p3',(12,2))
r1 = cursor.fetchall()
print(r1)


cursor.execute('select @_p3_0,@_p3_1')
r2 = cursor.fetchall()
print(r2)

cursor.close()
conn.close()