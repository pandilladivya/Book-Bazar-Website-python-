#!/usr/bin/env python3
import os
import cgi
import sqlite3
from http.cookies import *
path= '/var/www/html/bb.db'
con=sqlite3.connect(path)
cur=con.cursor()
form=cgi.FieldStorage()
print("Content-Type:text/html\n\n")

print("""<html>
<link rel="stylesheet" type="text/css" href="phomepage.css">
<head>
  
   <header>
   <nav>
   <table width=100%>
     <tr>
     <br><br>
      <center><h1><font size="7">BookBazaar</font></center>
        <tr><td></td></tr>
      <tr>
        <td bgcolor="orange">
        <br>
         <ul id="menu">
            <li><a href="abtus.py" style="text-decoration:none  text-size="1"><font size="4" ><b>About BookBazaar</b></font></a></li>
            <li><a href="contact.py" style="text-decoration:none  text-size="1" ><font size="4"><b>Contact Us</b></font></a></li>
            <li><a href="index.html"><font size="4"><b>hello""")

if 'HTTP_COOKIE' in os.environ:
 #print("hi")
 string_cookie=os.environ.get('HTTP_COOKIE')
 c=SimpleCookie()
 c.load(string_cookie)

 try:
  data=c['usr'].value;
  select="select name from registered where ( "+" hno= '"+data+"' )"
  cur.execute(select)
  list=cur.fetchone()
  #print(list)
  name=list[0]
  print(name)
  #print(data)
 except:
  print("The cookie was not set or has expired<br>");
  cgitb.handler()
print("""&#8628</b></font></a>
                  <ul>
                      <li><a href="logout.py"><font size="4"><b>Logout</b></font></a></li>
                 </ul>
            </li>
         </ul>
        </td>
      </tr>
     </table>
   </nav>
   </header>
 </head>

<body>
 <form method="post">
 <center>
   <fieldset>
     <legend><b><i><font size="6" color="blue">Books That You Require</font></i></b></legend>
     <table width=100%>
      <tr bgcolor="red">
        <td><font color="white" size="5"><b>Choose Deal</b></font></td>
        <td><font color="white" size="5"><b>Book Name</b></font></td>
        <td><font color="white" size="5"><b>Author</b></font></td>
        <td><font color="white" size="5"><b>Price</b></font></td>
        <td><font color="white" size="5"><b>Interests</b></font></td>
      </tr>""")
if 'HTTP_COOKIE' in os.environ:
    try :
        count=int(c['count'].value)
        for i in range(1,count+1):
            print("<tr>")
            radio="<td><input type='radio' name='choose' value= "+str(i)+"></td>"
            print(radio)
            for j in range(1,5):
                if (j==1):
                    
                    key="bname"+str(i)
                elif (j==2):
                    key="b_author"+str(i)
                elif (j==3):
                    key="b_price"+str(i)
                elif (j==4):
                    key="b_interests"+str(i)
                print("<td><font color='black' size='4'>"+c[key].value+"</font></td>")
            print("</tr>")
    except Exception as e:
        print(e)
    
print("""</table>
   </fieldset>
 </center><br>
 <input type="submit" id="pd" name="submit" value="Proceed to deal >>>">
 </form>
</body>
</html>
""")

deal="""
<html>
  <body onload="window.location='http://127.0.1.1/deal.py'">
  </body>
</html>
"""

if 'submit' in form:
    choice=form.getvalue('choose')
    if 'HTTP_COOKIE' in os.environ:
        c['choice']=choice
        #print(c['choice'].value)
        print(c.js_output())
        print(deal)

