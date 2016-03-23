#!/usr/bin/env python3
import os
import cgi
import sqlite3
import emailmsg
import nsm2
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
   <form id="fill" method="post">
   <center>
     <fieldset>
     <legend><font color="white" size="4">About Your Choice</legend>
       <table>
         <tr><td><font color="white">Book Title : </font></td>
         <td><font color="white">""")
if 'HTTP_COOKIE' in os.environ:
    title="bname"+c['choice'].value
    print(c[title].value)
print("""   </font></td></tr>
         <tr>
         <td><font color="white">Author :</td>
         <td><font color="white">""")
if 'HTTP_COOKIE' in os.environ:
    title="b_author"+c['choice'].value
    print(c[title].value)
print("""</font></td></tr>
        <tr>
          <td><font color="white">Seller's Price : </td>
          <td><font color="white">""")
if 'HTTP_COOKIE' in os.environ:
    title="b_price"+c['choice'].value
    print(c[title].value)
print("""</font></td>
        </tr>
        
        <tr><td>Year to which Book belongs to : </td>
        <td>""")
if 'HTTP_COOKIE' in os.environ:
    title="byear"+c['choice'].value
    print(c[title].value)
print("""
        </td>
        <tr><td>Semister to which Book belongs to : </td>
        <td>""")
if 'HTTP_COOKIE' in os.environ:
    title="bsem"+c['choice'].value
    if c[title].value!='0':
        print(c[title].value)
    else:
        print("---")
print("""</td>
        </tr>
        <tr>
        <td>Branch to which the Book belongs to : </td>
        <td>""")
if 'HTTP_COOKIE' in os.environ:
    title="b_branch"+c['choice'].value
    print(c[title].value)
print("""</td>
        </tr>
        <tr>
        <td>Subject to which the Book belongs to : </td>
        <td>""")
if 'HTTP_COOKIE' in os.environ:
    title="b_sub"+c['choice'].value
    print(c[title].value)
print("""</td>
        </tr>
        <tr>
         <td>Category of the Book: </td>
         <td>""")
if 'HTTP_COOKIE' in os.environ:
    title="b_cat"+c['choice'].value
    print(c[title].value)
print("""</td>
        </tr>
        <tr>
        <td>Number of interests for the Book : </td>
        <td>""")
if 'HTTP_COOKIE' in os.environ:
    title="b_interests"+c['choice'].value
    print(c[title].value)
print("""</td>
        </tr>
        <tr><td></td</tr>
        <tr><td><center><h3><font color="yellow"><u>SELLERS DETAILS</u></font></h3></center></td></tr>
        <tr><td>Name: </td>
        <td>""")
if 'HTTP_COOKIE' in os.environ:
    try:
        title="hno"+c['choice'].value
        select="select name from registered where (hno= '"+c[title].value+"' )"
        #print(select)
        cur.execute(select)
        data=cur.fetchall()
        print(data[0][0])
    except Exception as e :
        print(e)
        
print("""</td>
        </tr>
        <tr><td>Year: </td>
        <td>""")
if 'HTTP_COOKIE' in os.environ:
    try:
        title="hno"+c['choice'].value
        select="select syear from registered where (hno= '"+c[title].value+"' )"
        #print(select)
        cur.execute(select)
        data=cur.fetchall()
        print(data[0][0])
    except Exception as e :
        print(e)
        
print("""</td>
        </tr>
        <tr>
        <td>Branch: </td>
        <td>""")
if 'HTTP_COOKIE' in os.environ:
    try:
        title="hno"+c['choice'].value
        select="select branch from registered where (hno= '"+c[title].value+"' )"
        #print(select)
        cur.execute(select)
        data=cur.fetchall()
        print(data[0][0])
    except Exception as e :
        print(e)
print("""</td></tr>
         <tr>
         <td>Contact: </td>
         <td>""")
if 'HTTP_COOKIE' in os.environ:
    try:
        title="hno"+c['choice'].value
        select="select s_phno from registered where (hno= '"+c[title].value+"' )"
        #print(select)
        cur.execute(select)
        data=cur.fetchall()
        print(data[0][0])
    except Exception as e :
        print(e)
print("""</td>
         </tr>
         <tr>
          <td>Email: </td>
          <td>""")
if 'HTTP_COOKIE' in os.environ:
    try:
        title="hno"+c['choice'].value
        select="select email from registered where (hno= '"+c[title].value+"' )"
        #print(select)
        cur.execute(select)
        data=cur.fetchall()
        print(data[0][0])
    except Exception as e :
        print(e)
print("""</td></tr>
       </table>
     </fieldset>
   </center>
   <right>
    <fieldset>
    <legend><font color="maroon" size="5"><b>""")
if 'HTTP_COOKIE' in os.environ:
    try:
        title="hno"+c['choice'].value
        select="select name from registered where (hno= '"+c[title].value+"' )"
        #print(select)
        cur.execute(select)
        data=cur.fetchall()
        print(data[0][0])
    except Exception as e :
        print(e)
        
print(""" says:</b></font></legend><center><font color="maroon" size="4">""")
if 'HTTP_COOKIE' in os.environ:
    title="b_des"+c['choice'].value
    print(c[title].value)    
print("""</font></center></fieldset>
   </right><br><br>
    <input type="submit" id="pd" name="submit" value="Send Intrest Note>>>">
   </form>
 </body>
 </html>
""")

send="""
<html>
  <body onload="window.location='http://127.0.1.1/buy_done.py'">
  </body>
</html>
"""


if 'submit' in form :
    #print(c)
   
    if 'HTTP_COOKIE' in os.environ:
        #print("hi")
        try:
            hno="hno"+c['choice'].value
            bname="bname"+c['choice'].value

            update="update uploaded set interests=interests+1 where (hno= '"+c[hno].value+"' and bname= '"+c[bname].value+"' )"
            print(update)
            cur.execute(update)
            #con.commit()
            select="select b_hno from uploaded where (hno= '"+c[hno].value+"' and bname= '"+c[bname].value+"' )"
            cur.execute(select)
            b_hno=cur.fetchall()
            b_hno=b_hno[0][0]+c['usr'].value+','
            update="update uploaded set b_hno= '"+b_hno+"' where (hno= '"+c[hno].value+"' and bname= '"+c[bname].value+"' )"
            cur.execute(update)
            con.commit()
            print(update)
            
            
            select="select email from registered where (hno= '"+c[hno].value+"')"
            cur.execute(select)
            email=cur.fetchall()
            #print(select)
            msg1="Dear BookBazaar customer ,\nthe student with following details is interested in buying the book '"
            bname="bname"+c['choice'].value
            select="select name,syear,branch,s_phno from registered where (hno= '"+c['usr'].value+"' )"
            cur.execute(select)
            details=cur.fetchall()
            #print(email)
            #print(details)
            msg=msg1+c[bname].value+"'"+"that you have put in your BookBazaar STALL..."+"\n\nname : "+details[0][0]+"\nyear : "+str(details[0][1])+"\nbranch:"+details[0][2]+"\nContact : "+str(details[0][3])
            #print(email[0][0])
            #print(msg)
            un="9573205741"
            pwd="T6329H"
            select="select s_phno from registered where (hno= '"+c[hno].value+"' )"
            cur.execute(select)
            ph_no=cur.fetchall()
            emailmsg.emailms(email[0][0],msg)
            #nsm2.smscall(un,pwd,msg,ph_no[0][0])
            print(c.js_output())
            print(send)
        except Exception as e :
            print(e)
