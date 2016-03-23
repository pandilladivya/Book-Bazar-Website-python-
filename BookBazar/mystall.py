#!/usr/bin/env python3
import os
import cgi,cgitb
cgitb.enable()
from http.cookies import*


import sqlite3
path= '/var/www/html/bb.db'
con=sqlite3.connect(path)
cur=con.cursor()
form=cgi.FieldStorage()

#c=SimpleCookie()

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
            <li><a href="logged_in.py"><font size="4"><b>hello""")

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
 <center>
 <table width=70% height=70%>
 
 <tr>
 <td>
 <center>
   <button type="button"  style="width: 200px; height: 100px"><a href="editstall.py"  ><font size="5" > Remove Books From Mystall</font> </a></button>
 </center>
 </td>
 <td>
 <center>
   <button type="button" style="width: 200px; height: 100px"><a href="viewstall.py"><font size="5" >View Books On My Stall</font></a></button>
 </center>
 </td>
 </tr>
  
 
 </table></center>
 </body>""")
 

