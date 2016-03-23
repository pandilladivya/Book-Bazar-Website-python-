#!/usr/bin/env python3
import cgi
import sqlite3
import os

'''if 'HTTP_COOKIE' in os.environ:
 cookie_string=os.environ.get('HTTP_COOKIE')
 c=SimpleCookie()
 c.load(cookie_string)
 if 'username' in cookie_string:
  username=c['username'].value;

 else:
  username="fe";
  #print(html1);
  
else:
 username="14BD1A0594";
 #print(html1);
print(username)'''
path="/var/www/html/timetb.db"
con=sqlite3.connect(path)
cur=con.cursor()
x="14BD1A0594"

ttvar="select  branch,section,year,sem from student_details where id='"+x+"'"
print(ttvar)
#print(ttvar)
cur.execute(ttvar)
det=cur.fetchall()
print(det)
tabname=det[0][0]+det[0][1]+str(det[0][2])+str(det[0][3])
ft=det[0][0]+det[0][1]+str(det[0][2])+str(det[0][3])+'faculty'#csef21faculty 
form = cgi.FieldStorage()
print("Content-Type:text/html\n\n")
html1="""
<html>
<body>
 <form>
  <table border=1>"""

tr="<tr>"
td="<td>"
td_c="</td>"
trc="</tr>"
cur.execute("select * from timings")
b=cur.fetchall()
str1=""
for n in b:
    str1=str1+tr
    for m in n:
        x=str(m)
        str1=str1+td
        str1=str1+x
        str1=str1+td_c
    str1=str1+trc
sc="'>"
str2=""
dr="<select name='" 
drc="</select>"

op="<option value='"
opc="<option/>"
cur.execute("select * from  "+tabname)
a=cur.fetchall()
cur.execute("select sub from "+ft)
drp=cur.fetchall()
print(drp)

for j in a:
    str2=str2+tr
    for k in j:
        if k=='MONDAY' or k=='TUESDAY' or  k=='WEDNESDAY' or  k=='THURSDAY' or  k=='FRIDAY' or  k=='SATURDAY':
            str2=str2+td
            str2=str2+k
            str2=str2+td_c
        else:
            m=1
            str2=str2+td
            str2=str2+dr+'p'+str(m)+sc
            for p in drp:
                m+=1
                for q in p:
                    str2=str2+op+q+sc+q+opc
            str2=str2+drc
            str2=str2+td_c
    str2=str2+trc
        
htmlc='''</table>
</form>
</body>
</html>
'''

html=html1+str1+str2+htmlc
print(html.format(**locals()))
        
