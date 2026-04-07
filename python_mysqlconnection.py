import pymysql
conn=pymysql.connect(
    host="localhost",
    user="root",
    password="1234",
    database="pymysql_connection"
)

if (conn):
    print("connected successfully")
cursor=conn.cursor()
#all the operations are in cursor 

#cursor.execute(""" create table if not exists employee( id int primary key,name varchar(50),age int,department varchar(20),salary float)""")
#conn.commit()
#cursor.execute("insert into employee (id,name,age,department,salary) values(1,'Alice',29,'MCA'  ,20000)")
#cursor.execute("insert into employee  values(2,'Sanoop',23,'MBA'  ,20000)")
#cursor.execute("insert into employee  values(3,'Anju',23,'MA hindi'  ,30000)")
#cursor.execute("insert into employee  values(4,'maghi',22,'BBA'  ,20000)")
#conn.commit()

'''print("inserted successfully")
cursor.execute("select * from employee")
for i in cursor.fetchall():
    print(i)'''
cursor.execute("update employee set name='Ammu' where id=3")
cursor.execute("select * from employee")
for i in cursor.fetchall():
    print(i)
conn.commit()
cursor.execute("delete from employee  where id=3")
cursor.execute("select * from employee")
for i in cursor.fetchall():
    print(i)
conn.commit()
print("**********************************")
emp=(3,"riyas",24,"BCOM",25000)
cursor.execute("insert into employee (id,name,age,department,salary) values(%s,%s,%s,%s  ,%s)",emp)
conn.commit()
cursor.execute("select * from employee")
for i in cursor.fetchall():
    print(i)


cursor.close()
conn.close()
print("connection closed")

