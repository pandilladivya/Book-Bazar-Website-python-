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
 <form method="post">
   <fieldset>
     <legend><font size="6" color="white">STALL EDITOR :</font></legend><center>
     <table width=100%>
       <tr bgcolor="red">
          <td><font color="white">Edit </font></td>
          <td><font color="white">Book Title</font></td></tr>""")
if 'HTTP_COOKIE' in os.environ:
      select="select bname from uploaded where (hno='"+c['usr'].value+"')"
      cur.execute(select)
      books=cur.fetchall()
      row=0
      for i in books:
            row=row+1
            print("<tr><td><input type='radio' name='choose' value="+str(row)+"></td>")
            
            for j in i :
                key="ebname"+str(row)
                c[key]=j
                print("<td><font color='orange'>")
                print(j)
                print("</font></td>")
            print("</tr>")
print(""" 
     </table><center>
   </fieldset>
   <table width=100%>
     <tr>
       <td><input type="submit" name="del" id="pd" value="DELETE!!"></td>
       <td><input type="submit" name="edit" id="pd" value="EDIT >>"></td>
     </tr>
   </table>
 </form>
</body>
</html>""")

change="""
<html>
  <body onload="window.location='http://127.0.1.1/change.py'">
  </body>
</html>
"""

if 'del' in form :
    c['choice2']=form.getvalue('choose')
    ebname="ebname"+str(row)
    delete="delete from uploaded where(bname= '"+c[ebname].value+"' and hno= "+str(c['usr'].value)+")"
    cur.execute(delete)
    con.commit()

if 'edit' in form :
    c['choice2']=form.getvalue('choose')
    print(c.js_output())
    #print(change)
    
