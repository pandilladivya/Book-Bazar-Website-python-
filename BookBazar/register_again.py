#!/usr/bin/env python3
import os
import cgi
import cgitb
cgitb.enable()
import sqlite3
from http.cookies import *
path='/var/www/html/bb.db'
con=sqlite3.connect(path)
cur=con.cursor()
form=cgi.FieldStorage()
print("Content-Type:text/html")

print("""
<html>
  <link rel="stylesheet"  href="phomepage.css">
  <head>
   <header>
   <nav>
   <table width=100%>
   <tr>
      <br><br>
      <center><font size="7">BookBazaar</font><br></center>
      <p align=><marquee><font size="3">SHARE AND GAIN KNOWLEDGE WITH BookBazaar</font></marquee></p>
      </tr>
      <tr>
        <td bgcolor="orange">
           <h2><button type="button"><a href="abtus.py">About BookBazaar</a></button></h2>
        </td>
        <td bgcolor="orange">
         <h2><button type="button"><a href="contact.py">Contact Us</a></button></h2>
        </td>
      </tr>
     </table>
   </nav>
   </header>
 </head>
 <body><center><font size="5" color="red"> Password Doesnot Match With Confirmation</font></center>
      <center><form method="post">
      <table>
      
      <tr>
      <td>
       Name*:
       </td>
       <td> <input type="text" name="stname" required><br></td>
       </tr>
       <tr>
       <td>year*:</td>
       <td><input type="radio" name="year"  value=1 required>1st
              <input type="radio" name="year"  value=2 required>2nd
              <input type="radio" name="year"  value=3 required>3rd
              <input type="radio" name="year"  value=4 required>4th<br></td>
       </tr>
       <td>branch*</td>
       <td><input type="radio" name="branch" value="cse"required>cse
       <input type="radio" name="branch" value="it" required>it
       <input type="radio" name="branch" value="eie" required>eie
       <input type="radio" name="branch" value="ece" required>ece
       </td>
       <tr>
       </tr>
       <tr>       
       <td>sem*:</td>  
       <td><input type="radio" name="sem" value=1 required>1
             <input type="radio" name="sem" value=2 required>2<br></td>
       </tr>
       <tr>
       <td>phone number*:</td> 
       <td><input type="integer" name="phno"required><br></td>
       </tr>
       <tr>
       <td>email:</td> 
       <td><input type="email" name="email"><br></td>
       </tr>
       <tr>
          <td>
            password*:
          
          </td>
          <td> <input type="password" name="password" required><br></td>
          
       </tr>
       <tr>
           <td>re-enter password*:</td>
           <td><input type="password" name="repassword" required><br></td>
       </tr>
       </table>
       <input type="submit" name="submit" value="register">      
      </form>
       </center>
    </body>

</html>
""")

reg="""<html>
                     <body onload="window.location='http://127.0.1.1/register_again.py'">
                     </body>
               </html>
"""


class person_info:
    def __init__(self,stname,year,sem,phno,email,password,repassword,branch):
        self.stname=stname
        self.year=year
        self.sem=sem
        self.phno=phno
        self.email=email
        self.password=password
        self.repassword=repassword
        self.branch=branch
    try:
        
        def pcheck(self):
            
            if(self.password!=self.repassword):
                
                print(reg)
            else:
                self.register()
        def register(self):
            #cur.execute("")
            #cur.execute("select hno from currentreg;")
            #x=cur.fetchall()
            #hno=x[0]           
            if 'HTTP_COOKIE' in os.environ:
                string_cookie=os.environ.get('HTTP_COOKIE')
                c=SimpleCookie()
                c.load(string_cookie)
                print("hi")
                #data=c['usr'].value
                #print(data)
                cur.execute("insert into registered values(?,?,?,?,?,?,?,?)",(c['usr'].value,self.stname,self.year,self.sem,self.phno,self.email,self.password,self.branch,))
                con.commit()
                os.system('/var/www/html/logged_in.py')
    except Exception as e:
        print(e)
#print(register)
if 'submit' in form:
    if((form.getvalue('year')=='1' and form.getvalue('sem')!='0' ) or (form.getvalue('year')!='1' and form.getvalue('sem')=='0')):
        print(again)
    else :
        r=person_info(form.getvalue('stname'),form.getvalue('year'),form.getvalue('sem'),form.getvalue('phno'),form.getvalue('email'),form.getvalue('password'),form.getvalue('repassword'),form.getvalue('branch'))
        person_info.pcheck(r)
