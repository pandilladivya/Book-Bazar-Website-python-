#!/usr/bin/env python3
from http.cookies import*
import cgitb
cgitb.enable()
import cgi, os, sqlite3

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
   <marquee>AN INTEREST NOTE HAS BEEN SENT TO THE SELLER ....</marquee>
   <center><table width=100% height=80%>
   
      <tr>
         <td>
         <center>
        <a href="upload.py"><img src="upload-book-icon_1577827.jpg" alt="sorry"       style="width:300px;height:300px;border:0;">
        
        </a><br><br><br><font size="5" color="green"><b><i>UPLOAD A BOOK</i></b></font>
        </center>
         </td>
         <td>
         <center>
          <a href="search.py">
  <img src="buy2.png" alt="hii" style="width:320px;height:320px;border:0;">
</a><br><br><br><font size="5" color="green"><b><i>Buy</i></b></font>
         </center>
         </td>
         <td>
          <a href="viewstall.py">
  <img src="index.jpeg" alt="hii" style="width:320px;height:320px;border:0;">
</a><br><br><br><font size="5" color="green"><b><i>My stall</i></b></font>
         </td>
         </tr>
         
         
    </table></center>
 </body>
</html>"""
)
