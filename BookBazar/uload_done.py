#!/usr/bin/env python3
import os
import cgi
from http.cookies import*
form=cgi.FieldStorage()


import sqlite3
path= '/var/www/html/bb.db'
con=sqlite3.connect(path)
cur=con.cursor()
c=SimpleCookie()


print("Content-Type:text/html\r\n\n")
print("")
print("")
home="""<html>
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
      <tr><td></td></tr>
      <tr>
        <td bgcolor="orange">
        <br>
         <ul id="menu">
            <li><a href="abtus.py" style="text-decoration:none  text-size="1"><font size="4" ><b>About BookBazaar</b></font></a></li>
            <li><a href="contact.py" style="text-decoration:none  text-size="1" ><font size="4"><b>Contact Us</b></font></a></li>
         </ul>
        </td>
      </tr>
     </table>
   </nav>
   </header>
 </head>
<body>
   <form method="get">
    <nav>
     <marquee><marquee>THE BOOK HAS BEEN SUCCESSFULLY UPLOADED (TO EDIT DETAILS.. ,VISIT "MY STALL")</marquee></marquee> 
    <table width=100% height=70%>
         <tr>
           <td width=70%>
          <center> <img src="img1.png" alt="sorry ! pic not available .." ></center>
         </td>
         <td width=30%>
             <center>
              <fieldset>
                 <legend><italic><b>Login : </b></italic></legend>
                 <table>
                     <tr>
                        <td>
                         <b>hallticket no :</b>
                         </td>
                         <td>
                         <input type="text" name="hno">
                        </td
                     </tr>
                     <tr>
                        <td>
                         <b>password:</b>
                         </td>
                         <td>
                         <input type="password" name="password">
                        </td>
                     </tr>
                 </table>
                  <input type="submit" name="submit" value="Sign In">
                </fieldset>
                <marquee><h3>Not yet a member of BookBazar </h3></marquee><br>
                <button type="button"><a href="hno_verify.py">Register Now</a></button>
             </center>
          </td>
         </tr>
    </table>
    </nav>
   </form>
</body>
 </html>"""

login="""
<html>
  <body onload="window.location='http://127.0.1.1/logged_in.py'">
  </body>
</html>
"""

def checklogin():
    
    try:
        
        cur.execute("select hno,password from registered")
        listing=cur.fetchall()
        flag=0
        for i in listing:
            if(a1==i[0] and a2==i[1]):
                
                print("Login Successful")
                flag=1
                c['usr']=i[0]
                #print(c['usr'])
                #print(c)
                #print("Content-Type:text/html\n\n")
                print(c.js_output())
                print(login)
                break
            
        if(flag==0):
            
            print("Login Failed")
            os.system('/var/www/html/home_again.py')
        
    except Exception as e:
        print(e)
    finally:
        con.close()


a1=form.getvalue('hno')
a2=form.getvalue('password')

if 'submit' in form:
        checklogin()

if a1==None:
    
    print(home.format(**locals()))
                        
    



