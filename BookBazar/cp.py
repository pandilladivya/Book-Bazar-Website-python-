#!/usr/bin/env python3
import cgi
import sqlite3
try:
    path='/var/www/html/test1.db'
    con=sqlite3.connect(path)
    cur=con.cursor()
   # cur.execute("drop table emp")
    cur.execute("create table emp1(eid int ,ename varchar(20))")
    form=cgi.FieldStorage()
    print("Content-Type: text/html")
    htmlFormat= '''<html> <Title> The Times Now </Title> <body> <form method="POST"> Employee ID:<input type="text" name="num1" value=0 /></br>
    Employee Name:<input type="text" name="num2" value=0 /></br>
    <input type="submit" value="Enter"/> </br>
    <p> Employee Deatils {data} </p>
    </form></body>
    </html>'''
    num11=form.getvalue("num1",'0')
    num22=form.getvalue("num2",'0')
    n1=int(num11)
    n2=str(num22)
    cur.execute("insert into emp1 values(?,?)",(n1,n2))
    cur.execute("select *from emp1")
    data=cur.fetchall()
    con.commit()
    con.close()
    print(htmlFormat.format(**locals()))
except:
    print("Error")

