
import mysql.connector

mydb=mysql.connector.connect(host="localhost",user="jay",passwd="dj141199",database="db1")

mycursor=mydb.cursor();

print(mydb.connection_id)

import sys
print(sys.path)

# ['D:\\FRAS', 'C:\\Users\\DJ\\AppData\\Local\\Programs\\Python\\Python38-32\\python38.zip', 'C:\\Users\\DJ\\AppData\\Local\\Programs\\Python\\Python38-32\\DLLs', 'C:\\Users\\DJ\\AppData\\Local\\Programs\\Python\\Python38-32\\lib', 'C:\\Users\\DJ\\AppData\\Local\\Programs\\Python\\Python38-32', 'C:\\Users\\DJ\\AppData\\Roaming\\Python\\Python38\\site-packages', 'C:\\Users\\DJ\\AppData\\Roaming\\Python\\Python38\\site-packages\\win32', 'C:\\Users\\DJ\\AppData\\Roaming\\Python\\Python38\\site-packages\\win32\\lib', 'C:\\Users\\DJ\\AppData\\Roaming\\Python\\Python38\\site-packages\\Pythonwin', 'C:\\Users\\DJ\\AppData\\Local\\Programs\\Python\\Python38-32\\lib\\site-packages']

# mycursor.execute("create database db1")

# mycursor.execute("show databases")
# for u in mycursor:
# 	print(u);


# q="create table student_details(name varchar(100),id int)"

# mycursor.execute(q)

# q2="insert into student_details(name,id) values (%s,%s)" #query

# s=("Rock","86")
# mycursor.execute(q2,s) #to insert single record

# t=[("Jay","204"),("Sohil","227"),("Chirayu","250")]
# mycursor.executemany(q2,t)#to insert multiple records
# mydb.commit()
# print("done")

# q3="select *from student_details"
# mycursor.execute(q3)
# result=mycursor.fetchall()

# for rec in result:
#     print(rec)

# q4="UPDATE student_details SET id=id+1 where id<200"
# mycursor.execute(q4)
# mydb.commit()


# q5="DELETE FROM student_details WHERE id>200"
# mycursor.execute(q5)
# mydb.commit()






