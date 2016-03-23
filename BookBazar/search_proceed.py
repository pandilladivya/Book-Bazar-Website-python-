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
   
     <center>
            <fieldset><legend align="center">Details Of The Book To Search</legend>
                <center>
                  <form method="post">
                    <table><font size="4">
                       <tr>
                           <td>year*:
                           </td>
                           <td>""")
if 'HTTP_COOKIE' in os.environ:
    byear=int(c['sbyear'].value)
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

print("""</td>
                       </tr>
                       <tr>
                           <td>sem*:
                           </td>
                           <td>
                           """)

if 'HTTP_COOKIE' in os.environ:
    bsem=int(c['sbsem'].value)
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
    b_branch=c['sb_branch'].value
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



print("""</select>
                          </td>
                       </tr>
                       <tr>
                          <td>
                            Subject*:
                          </td>
                          <td>
                               <select  name="subjects" >""")
if 'HTTP_COOKIE' in os.environ:
    substr="select subject from sub_list where (year= "+str(byear)+" and sem= "+str(bsem)+" and branch= '"+str(b_branch)+"'  ) "
    cur.execute(substr)
    subs=cur.fetchall()
    string=""
    for i in subs :
        for j in i :
            
            print("<option>"+j+"</option>")
   
                                  
print("""</select>
                          </td>
                       </tr>
                       <tr>
                            <td>Category :</td>
                            <td>
                              <input type="checkbox" name="tb" value="Textbook">Textbook<br>
                              <input type="checkbox" name="guide" value="Guide">Guide<br>
                              <input type="checkbox" name="all" value="All in One">All in One<br>
                              <input type="checkbox" name="mp" value="Model Papers">Model Papers<br>
                              <input type="checkbox" name="notes" value="Notes">Notes<br>

                            </td>
                       </tr>
                       <tr>
                          <td>
                          <center><input style="background-color:yellow" type="submit" name="submit" value="search">   
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
go="""
<html>
  <body onload="window.location='http://127.0.1.1/search_result.py'">
  </body>
</html>
"""

notFound="""
<html>
  <body onload="window.location='http://127.0.1.1/notFound.py'">
  </body>
</html>
"""

if 'HTTP_COOKIE' in os.environ:
    class search:
        def __init__(self,byear,bsem,b_branch,sub):
            c['sb_sub']=sub
            given=[]
            chosen=[]
            given.append('tb')
            given.append('guide')
            given.append('all')
            given.append('mp')
            given.append('notes')
            for i in given:
                if form.getvalue(i)!=None :
                    chosen.append(i)
            #print(chosen)
            select1="select * from uploaded where ( byear= "+byear+" and bsem= "+bsem+" and b_branch= '"+b_branch+"' and b_sub= '"+sub+"' and ( "
            l=len(chosen)
            #print(l)
            for j in range(0,l-1):
                #print(form.getvalue(chosen[j]))
                
                select1=select1+"b_category= '"+form.getvalue(chosen[j])+"' or "
            select=select1+" b_category= '"+form.getvalue(chosen[l-1])+"'"+") and hno!= '"+c['usr'].value+"')"
            print(select)
            cur.execute(select)
            result=cur.fetchall()
            print(result)
            if len(result)==0:
                print(notFound)
            count=0
            for i in result:
                count=count+1
                p=0
                for j in i :
                    p=p+1
                    if(p==1):
                        key="hno"+str(count)
                    elif(p==2):
                        key="bname"+str(count)
                    elif(p==3):
                        key="b_author"+str(count)
                    elif(p==4):
                        key="byear"+str(count)
                    elif(p==5):
                        key="bsem"+str(count)
                    elif(p==6):
                        key="b_branch"+str(count)
                    elif(p==7):
                        key="b_sub"+str(count)
                    elif(p==8):
                        key="b_des"+str(count)
                    elif(p==9):
                        key="b_cat"+str(count)
                    elif(p==10):
                        key="b_price"+str(count)
                    elif(p==11):
                        key="b_img"+str(count)
                    elif(p==12):
                        key="b_interests"+str(count)
                    print(key)
                    c[key]=j
                
            c['count']=count
            print(c['count'].value)
            print(c.js_output())
            print(go)
                

    if 'submit' in form:
        #print(c['sbyear'].value,c['sbsem'].value,c['sb_branch'].value,form.getvalue('subjects'))
        s=search(c['sbyear'].value,c['sbsem'].value,c['sb_branch'].value,form.getvalue('subjects'))

