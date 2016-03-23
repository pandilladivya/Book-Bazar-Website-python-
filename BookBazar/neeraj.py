#!/usr/bin/env python3
import cgi
import sqlite3
import os
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
x="'14BD1A0501'"
cur.execute("select * from student_details where id="+x)
tm=cur.fetchall()
print(tm)

print("Content-Type: text/html\n\n")
html1="""
<html>
<body>
 <form>
  <table border=1>"""

tr="""
<tr>
"""
td="<td>"
td_c="</td>"
trc="</tr>"
cur.execute("select * from timings")
b=cur.fetchall()
str1=''
for n in b:
    str1=str1+tr
    for m in n:
        x=str(m)
        str1=str1+td
        str1=str1+x
        str1=str1+td_c
    str1=str1+trc
cur.execute("select * from "+tabname)
a=cur.fetchall()

str2=""
for j in a:
    str2=str2+tr
    for k in j:
        str2=str2+td
        str2=str2+k
        str2=str2+td_c
    str2=str2+trc
        
htmlc='''
</table>
</form>
</body>
</html>
'''

html=html1+str1+str2+htmlc
print(html.format(**locals()))
        
