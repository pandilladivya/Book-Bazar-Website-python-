#!/usr/bin/env python3
from http.cookies import*
import cgitb
cgitb.enable()
import cgi, os, sqlite3

form=cgi.FieldStorage()

path= '/var/www/html/bb.db'
con=sqlite3.connect(path)
cur=con.cursor()

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
     <legend><font size="6" color="white"><italic><b>MY STALL:</b></italic></font></legend>
     <table width=100%>
       <tr bgcolor="red">
         <td><font color="white">Choose Deal</font></td>
         <td><font color="white">Book Title</font></td>
         <td><font color="white">My Price</font></td>
         <td><font color="white">Interests</font></td>
       </tr>""")
if 'HTTP_COOKIE' in os.environ:
    select="select bname,b_price,interests,b_hno from uploaded where(hno= '"+c['usr'].value+"')"
    cur.execute(select)
    stall=cur.fetchall()
    if len(stall)==0:
        print(go)
    else :
        row=0
        for i in stall:
            row=row+1
            p=0
            print("<tr><td><input type='radio' name='choose' value="+str(row)+"></td>")
            for j in i:
                print("<td><font color='orange'>")
                p=p+1
                if(p==1):
                    key="bt"+str(row)
                elif(p==2):
                    key="price"+str(row)
                elif(p==3):
                    key="interests"+str(row)
                
                c[key]=j
                if (p<4):
                    print(j)            
                    print("</td>")
            print("</tr>")
        c['row']=row

sell="""
<html>
  <body onload="window.location='http://127.0.1.1/sell.py'">
  </body>
</html>
"""

print("""</table>
   </fieldset><br><br>
    <input type="submit" id="pd" name="submit" value="See Details >>">
  </form>
 </body>
 </html>""")


if 'submit' in form :
    c['choice']=form.getvalue('choose')
    print(c.js_output())
    print(sell)
