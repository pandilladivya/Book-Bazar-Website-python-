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
 <form  enctype="multipart/form-data" method="get">
 <center>
 <table>
     <tr>
     <td>
      Book Name:
     </td>
        <td><input type="text" name="bname" value=""")

if 'HTTP_COOKIE' in os.environ:
    bname=c['bname'].value
    print(bname)

print("""required  disabled></td>
     </tr>
     <tr>
       <td>
         Author:
       </td>
     <td><input type="text" name="author" value= """)

if 'HTTP_COOKIE' in os.environ:
    b_author=c['b_author'].value
    print(b_author)

print("""required disabled></td>
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
     <td>""")

if 'HTTP_COOKIE' in os.environ:
    byear=int(c['byear'].value)
    if byear==1:
        print("""<input type="radio" name="year"  value=1 required selected disabled checked="checked">1
      <input type="radio" name="year"  value=2 required disabled>2
      <input type="radio" name="year" value=3 required disabled>3
      <input type="radio" name="year" value=4 required disabled>4""")
    elif byear==2:
        print("""<input type="radio" name="year"  value=1 required  disabled>1
      <input type="radio" name="year"  value=2 required selected disabled checked="checked">2
      <input type="radio" name="year" value=3 required disabled>3
      <input type="radio" name="year" value=4 required disabled>4""")
    elif byear==3:
        print("""<input type="radio" name="year"  value=1 required disabled>1
      <input type="radio" name="year"  value=2 required disabled>2
      <input type="radio" name="year" value=3 required selected  disabled checked="checked">3
      <input type="radio" name="year" value=4 required disabled>4""")
    elif byear==4:
        print("""<input type="radio" name="year"  value=1 required disabled>1
      <input type="radio" name="year"  value=2 required disabled>2
      <input type="radio" name="year" value=3 required disabled>3
      <input type="radio" name="year" value=4 required selected   disabled checked="checked">4""")

print("""    
     </td>
     </tr>
     <tr>
       <td>
         Sem :
       </td>
       <td>""")
if 'HTTP_COOKIE' in os.environ:
    bsem=int(c['bsem'].value)
    if bsem==0:
        print("""<input type="radio" name="sem" required value=0 selected disabled checked="checked">0
        <input type="radio" name="sem" required value=1 disabled>1
        <input type="radio" name="sem" required value=2 disabled>2 """)
    elif bsem==1:
        print("""<input type="radio" name="sem" required value=0  disabled>0
        <input type="radio" name="sem" required value=1 selected disabled checked="checked">1
        <input type="radio" name="sem" required value=2 disabled>2 """)
    elif bsem==2:
        print("""<input type="radio" name="sem" required value=0  disabled>0
        <input type="radio" name="sem" required value=1 disabled>1
        <input type="radio" name="sem" required value=2 selected disabled checked="checked">2""")
    
print("""       </td>
     </tr>
     <tr>
       <td>
         Branch :
       </td>
       <td>
      """)
if 'HTTP_COOKIE' in os.environ:
    b_branch=c['b_branch'].value
    print("""<select  name="branch" value={branch1} value= """)
    print(b_branch)
    if b_branch=="cse" :
        print("""required disabled>
           <option>cse </option>""")
    if b_branch=="ece" :
        print("""required disabled>
           <option>ece </option>""")    
    if b_branch=="it" :
        print("""required disabled>
           <option>it </option>""")
    if b_branch=="eie" :
        print("""required disabled>
           <option>eie </option>""")

print(""" </select>
       </td>
        </tr>
        <tr>
       <td>
        subject :
       </td>
       <td>
        <select  name="subject"> """)


if 'HTTP_COOKIE' in os.environ:
    substr="select subject from sub_list where (year= "+str(byear)+" and sem= "+str(bsem)+" and branch= '"+str(b_branch)+"'  ) "
    cur.execute(substr)
    subs=cur.fetchall()
    #print(type(byear))
    #print(type(bsem))
    #print(type(b_branch))
    #print(subs)
    string=""
    for i in subs :
        for j in i :
            
            print("<option>"+j+"</option>")
    #print(string)
print("""
     </select>
        
       </td>
     </tr>
     <tr>
      <td>give description</td>
        <td><textarea rows="5" cols="50" name="description"  >
      </textarea></td>
     </tr>
     <tr>
      <td>
      category : 
      </tb>
      <td> 
        <input type="radio" name="cat" value="Textbook" required >Textbook<br>
        <input type="radio" name="cat" value="Guide" required >Guide<br>
        <input type="radio" name="cat" value="All in One" required >All in One<br>
        <input type="radio" name="cat" value="Model Papers" required >Model Papers<br>
        <input type="radio" name="cat" value="Notes" required >Notes<br>
      </td>
     </tr>
     <tr>
       <td>
        your price :
       </td>
       <td>
       <input type="number" name="price" >
       </td>
     </tr>
     <tr>
      <td>
        <input type="file" name="preview" accept="image/*" >
      </td>
      <td>
      <button type="submit" name="upload" value="upload"  >upload</button>
      </td>
     </tr>
     </table>
     </fieldset></center>
     </td>
     
     </tr>
     
</table></center>
</form>
</body>
</html>""")

go="""
<html>
  <body onload="window.location='http://127.0.1.1/upload_done.py'">
  </body>
</html>
"""


class book:
    def __init__(self,subject,description,cat,price):
        self.subject=subject
        self.description=description
        self.cat=cat
        self.price=price
        img=form.getvalue('preview')
        self.img=img
        print(self.img)
        if 'HTTP_COOKIE' in os.environ:
               hno=c['usr'].value
               zero=0
               empty=""
               new_rec="insert into uploaded values('"+hno+"','" + bname+"','"+b_author+"',"+str(byear)+","+str(bsem)+",'"+b_branch+"','"+self.subject+"','"+self.description+"','"+self.cat+"',"+str(self.price)+",'"+self.img+"',"+str(zero)+", '')"
               print(new_rec)
               cur.execute(new_rec)#hor,byear,bsem,b_branch,self.subject,self.description,self.cat,self.price,self.img,))
               con.commit()
               print(go)


if 'upload' in form and form.getvalue('subject')!=None :
    b=book(form.getvalue('subject'),form.getvalue('description'),form.getvalue('cat'),form.getvalue('price'))
    


