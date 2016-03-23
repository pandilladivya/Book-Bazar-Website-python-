#!/usr/bin/env python3
import os
import cgi
import sqlite3
from http.cookies import*
c=SimpleCookie()
path= '/var/www/html/bb.db'
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
   <body><center><font color="red">The Entered Hallticket Doesnot Belongs To KMIT<br>If It Does, Then Try Again</font></center>
     <form>
      
        <nav><br><br><br><br><br><br><center>
        
          hallticket number:<input type="text" name="hno">
          <input  type="submit" name="submit" value="Proceed">
        </center></nav>
     </form>
   
   </body>

</html>
""")

go1="""<html>
                     <body onload="window.location='http://127.0.1.1/hnoverifypage(1).py'">
                     </body>
               </html>
"""
go2="""<html>
                     <body onload="window.location='http://127.0.1.1/hnoverify(2).py'">
                     </body>
               </html>
"""
reg="""<html>
                     <body onload="window.location='http://127.0.1.1/register.py'">
                     </body>
               </html>
"""

class hnoverify:
    def __init__(self,hno):
        self.hno=hno
    try:
        def htverify(self):
            #cur.execute("drop table currentreg;")
            #cur.execute("create table currentreg(hno varchar)")
            #cur.execute("insert into currentreg values(?);",(self.hno,))
            #cur.execute("select hno from hnos;")
            c['usr']=self.hno
            listing=cur.fetchall()
            flag=0
            #print(listing)
            if a1[2]=='B' and a1[3]=='D' and len(a1)==10:
                
                self.regverify()
                print("if")
            else:
                print(go1)
                print("else")
            '''for i in listing:
               #print(i[0])
               
                   
               if(self.hno==i[0]):
                  #flag=1
                  self.regverify()
                  break
            else:
                  print(go1)'''
            
                
        def regverify(self):
            cur.execute("select hno from registered;")
            listing=cur.fetchall()
            for i in listing:
                if(self.hno==i[0]):
                    print("already a member")
                    print(go2)
                    break
            else:
                   print(c)
                   print("Content-Type:html/text\n\n")
                   print(c.js_output())
                   print(reg)
    except Exception as e:
        print(e)

a1=str(form.getvalue('hno'))
if 'submit' in form :
    h=hnoverify(a1)
    hnoverify.htverify(h)

