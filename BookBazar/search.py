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
            <fieldset><legend align="center">Details Of The Book To Search</legend>
                <center>
                  <form method="post">
                    <table><font size="4">
                       <tr>
                           <td>year*:
                           </td>
                           <td>
                             <input type="radio" name="year" value=1 required>1
                             <input type="radio" name="year" value=2 required>2
                             <input type="radio" name="year" value=3 required>3
                             <input type="radio" name="year" value=4 required>4
                           </td>
                       </tr>
                       <tr>
                           <td>sem*:
                           </td>
                           <td>
                           <input type="radio" name="sem" value=0 required>0
                           <input type="radio" name="sem" value=1 required >1
                           <input type="radio" name="sem" value=2 required>2 (if 1st year select 0)
                           </td>
                       </tr>
                       <tr>
                          <td>Branch*:
                          </td>
                          <td>
                          <select  name="branch" >
                               <option>cse</option>
                               <option>it</option>
                               <option>ece</option>
                               <option>eie</option>
                          </select>
                          </td>
                       </tr>
                         <tr><td></td><td></td></tr>
                           <tr><td></td><td></td></tr>
                       <tr><td></td><td><input type="submit" name="proceed" value="Proceed"></td></tr>
                       <tr><td></td><td></td></tr>
                         <tr><td></td><td></td></tr>
                       <tr>
                          <td>
                            Subject*:
                          </td>
                          <td>
                               <select  name="subjects" disabled>
                                  <option>subject1</option>
                                  <option>subject2</option>
                                  <option>subject3</option>
                                  <option>subject4</option>
                               </select>
                          </td>
                       </tr>
                       <tr>
                            <td>Category :</td>
                            <td>
                              <input type="radio" name="cat" required disabled>Textbook<br>
                              <input type="radio" name="cat" required disabled>Guide<br>
                              <input type="radio" name="cat" required disabled>All in One<br>
                              <input type="radio" name="cat" required disabled>Model Papers<br>
                             <input type="radio" name="cat" required disabled>Notes<br>
                            </td>
                       </tr>
                       <tr>
                          <td>
                          <center><button style="background-color:yellow" type="submit" disabled>
                            <img scr="6.jpg">
                          search</button>
                          </center></td> 
                       </tr>
                       </font>
                    </table>
                  </form>  
                </center>
            </fieldset>
     </center> 
 </body>

</html>
""")


proceed="""<html>
  <body onload="window.location='http://127.0.1.1/search_proceed.py'">
  </body>
</html>
"""

again="""<html>
  <body onload="window.location='http://127.0.1.1/search_again.py'">
  </body>
</html>
"""
class book:
    def __init__(self,byear,bsem,b_branch):
        self.byear=byear
        self.bsem=bsem
        self.b_branch=b_branch
        if 'HTTP_COOKIE' in os.environ:
            c['sbyear']=self.byear
            c['sbsem']=self.bsem
            c['sb_branch']=self.b_branch
            print(c)
            print(c.js_output())
            print(proceed)

if 'proceed' in form :
    if ((form.getvalue('year')=='1' and form.getvalue('sem')!='0') or (form.getvalue('year')!='1' and form.getvalue('sem')=='0') ):
            print("hi")
            print(c)
            print(c.js_output())
            print(again)

    b=book(form.getvalue('year'),form.getvalue('sem'),form.getvalue('branch'))
