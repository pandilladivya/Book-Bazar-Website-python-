#!/usr/bin/env python
import cgi
import sqlite3
import os
import urllib.request
path="/var/www/html/data.db"
con=sqlite3.connect(path)
cur=con.cursor()
#cur.execute("create table login(un varchar(30) primary key, pwd varchar(10))")
form = cgi.FieldStorage()
def checklogin():
    
    try:
        #cur.execute("insert into login values('kmit','kmit123')")
        #cur.execute("insert into login values('kmit1','kmit1234')")
        #con.commit()
        cur.execute("select * from login")
        listing=cur.fetchall()
        flag=0
        for i in listing:
            
            if(a1==i[0] and a2==i[1]):
                print("Login Successful")
                flag=1
                os.system('/var/www/html/home.py')
                
                break
        if(flag==0):
            print("Login Failed")
           
        
    except:
        print("Error")
    finally:
        con.close()      
    
print ("Content-Type: text/html\n\n")
html = """
<html>
<body>
   <form method="get"  >
      <p>
         User name: <input type="text" name="un"> </br>
         Password : <input type="text" name="pwd">
         </p>
      
      <p>
         <input type="submit" name='myfunc'   value="Submit">       </p>
          <p><input type="submit" name='exit'   value="exit">       </p>
      </form>
      </body>
</html>"""


a1=form.getvalue("un")
a2=form.getvalue("pwd")

if 'myfunc' in form:
        checklogin()
    
    
if 'exit' in form:
    print("Login Failed") 
if a1==None:
    print(html.format(**locals()))
