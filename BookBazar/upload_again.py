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
<link rel="stylesheet"  href="phomepage.css">
<head>
  
   <header>
   <nav>
   <table width=100%>
     <tr>
     <br><br>
      <center><h1><font size="7">BookBazaar</font></center>
      <p align="right"><font size="3">hello""") 
      
         


    
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

print("""</p></font></tr>

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
 <body>
 <form method="get">
 <center>
 <table>
     <tr>
     <td>
      Book Name:
      </td>
        <td><input type="text" name="bname"  required></td>
     </tr>
     <tr>
       <td>
         Author:
       </td>
     <td><input type="text" name="author" required></td>
     </tr>
     <tr>
       <td> 
       <center>
       <fieldset>
       <legend align="center">
           Academic Details of the Book
       </legend>
     
     <table>
     <tr>
     <td>
      Year :
     </td>
     <td>
      <input type="radio" name="year"  value=1 required>1
      <input type="radio" name="year"  value=2 required>2
      <input type="radio" name="year" value=3 required>3
      <input type="radio" name="year" value=4 required>4
     </td>
     </tr>
     <tr>
       <td>
         Sem :
       </td>
       <td>
        <input type="radio" name="sem" required value=0>0
        <input type="radio" name="sem" required value=1>1
        <input type="radio" name="sem" required value=2>2 <font color="red">(if 1st year select 0)</font>
       </td>
     </tr>
     <tr>
       <td>
         Branch :
       </td>
       <td>
         <select  name="branch">
          <option>cse</option>
          <option>it</option>
          <option>ece</option>
          <option>eie</option>
         </select>
       </td>
       <td>
           <center><input type="submit" name="proceed" value="Proceed"></center>
       </td>
     </tr>
     <tr>
       <td>
        subject :
       </td>
       <td>
        <select  name="subject" disabled>
         <option>Mathematical Methods</option>
         <option>Physics</option>
         <option>Chemistry</option>
         <option>C-programming</option>
         <option>English</option>
         <option>M1</option>
         
        </select>
        
       </td>
     </tr>
     <tr>
      <td>give description</td>
        <td><textarea rows="5" cols="50" name="description"  disabled>
      </textarea></td>
     </tr>
     <tr>
      <td>
      category : 
      </tb>
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
        your price :
       </td>
       <td>
       <input type="number" name="price" disabled>
       </td>
     </tr>
     <tr>
      <td>
        <input type="file" name="preview" accept="image/*" disabled>
      </td>
      <td>
      <button type="submit" name="upload" value="upload"  disabled>upload</button>
      </td>
     </tr>
     </table>
     </fieldset></center>
     </td>
     
     </tr>
     
</table></center>
</form>
</body>
</html>
 """) 

proceed="""<html>
  <body onload="window.location='http://127.0.1.1/upload_proceed.py'">
  </body>
</html>
"""

again="""<html>
  <body onload="window.location='http://127.0.1.1/upload_again.py'">
  </body>
</html>"""

class book:
  def __init__(self,bname,b_author,byear,bsem,b_branch):
        self.bname=bname
        self.b_author=b_author
        self.byear=byear
        self.bsem=bsem
        self.b_branch=b_branch
        
  try : 
     def upload(self):
       if 'HTTP_COOKIE' in os.environ :
        string_cookie=os.environ.get('HTTP_COOKIE')
        c=SimpleCookie()
        c.load(string_cookie)
        c['bname']=self.bname
        c['b_author']=self.b_author
        c['byear']=self.byear
        c['bsem']=self.bsem
        c['b_branch']=self.b_branch
        #print(c['byear'])
        print(c)
        print("Content-Type:text/html\n\n")
        print(c.js_output())
        print(proceed)
  except Exception as e:
      print(e)
        


b=book(form.getvalue('bname'),form.getvalue('author'),form.getvalue('year'),form.getvalue('sem'),form.getvalue('branch'))
if 'proceed' in form :
    if ((form.getvalue('year')=='1' and form.getvalue('sem')!='0') or (form.getvalue('year')!='1' and form.getvalue('sem')=='0') ):
            print("hi")
            print(c)
            print(c.js_output())
            print(again)
    book.upload(b)
