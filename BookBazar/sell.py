#!/usr/bin/env python3
from http.cookies import*
import emailmsg
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
   <form>
   <fieldset>
     <legend><font size="6" color="white"><b><italic>Buyers :</italic></b></font></legend>
     <table width=100%>
       <tr bgcolor="red">
         <td><font color="white">Deal with </font></td>
         <td><font color="white">Name</font></td>
         <td><font color="white">Year</font></td>
         <td><font color="white">Branch</font></td>
         <td><font color="white">Semister</font></td>
         <td><font color="white">Contact</font></td>
         <td><font color="white">Email</font></td>
       </tr>""")
if 'HTTP_COOKIE' in os.environ:
    bt='bt'+c['choice'].value
    price='price'+c['choice'].value
    select="select b_hno from uploaded where (hno= '"+c['usr'].value+"' and bname= '"+c[bt].value+"' and b_price= "+str(c[price].value)+")"
    #print(select)
    cur.execute(select)
    buyers=[]
    b_hno=cur.fetchall()
    #print(b_hno[0][0])
    buyer=""
    for i in b_hno[0][0]:
        if(i==','):
            buyers.append(buyer)
            buyer=""
        else:
            buyer=buyer+i
    #print(buyers)
    
    for i in buyers :
        select="select name,syear,branch,ssem,s_phno,email from registered where(hno= '"+i+"')"
        cur.execute(select)
        data=cur.fetchall()
        #print(data)
        print("<tr><td><input type='radio' name='choice1' value="+i+"></td>")
        for j in range(1,8):
            print("<td><font color='orange'>")
            if(j==1):
                print(data[0][0])
            elif(j==2):
                print(data[0][1])
            elif(j==3):
                print(data[0][2])
            elif(j==4):
                print(data[0][3])
            elif(j==5):
                print(data[0][4])
            elif(j==6):
                print(data[0][5])
            print("</font></td>")
        print("</tr>")
            
            
        
        
            
        

print("""</table>
   </fieldset>
 </body>
   <input type="submit" id="pd" name="submit" value="< Confirm Deal >">
 </form>
</html>""")

view="""
<html>
  <body onload="window.location='http://127.0.1.1/view_done.py'">
  </body>
</html>
"""

if 'submit' in form :
    bt='bt'+c['choice'].value
    price='price'+c['choice'].value
    msg1="Dear BookBazaar customer ,\n your request for the book '"+c[bt].value+"' has been confirmed by "
    select="select name from registered where (hno='"+c['usr'].value+"')"
    cur.execute(select)
    name=cur.fetchall()
    select="select email from registered where (hno='"+c['usr'].value+"')"
    cur.execute(select)
    email=cur.fetchall()
    select="select s_phno from registered where (hno='"+c['usr'].value+"')"
    cur.execute(select)
    phno=cur.fetchall()
    msg=msg1+name[0][0]+"\n\nYou can contact him with : \nEmail:"+email[0][0]+" \nmobile number : "+str(phno[0][0])
    bhno=form.getvalue('choice1')
    select="select email from registered where (hno='"+bhno+"')"
    cur.execute(select)
    email=cur.fetchall()
    emailmsg.emailms(email[0][0],msg)

    delete="delete from uploaded where(bname= '"+c[bt].value+"' and b_price= "+str(c[price].value)+")"
    cur.execute(delete)
    con.commit()
    
    print(c.js_output())
    print(view)
