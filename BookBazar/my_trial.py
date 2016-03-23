#!/usr/bin/env python3
import cgi
import os
import codecs
from http.cookies import*

import sqlite3
path= '/var/www/html/bb.db'
con=sqlite3.connect(path)
cur=con.cursor()


form=cgi.FieldStorage()

print("Content-Type:text/html\n\n")
print(
      """
    <html>
      <body>
       <form enctype="multipart/form-data" method="get">
        <select name="drop" >
          <option>5star</option>
          <option>Munch</option>
          <option>cadbury</option>
          <option>Kurkure</option>
        </select>
        <br>
         <input type="file" name="preview" accept="image/*" >
         <input type="submit" name="submit" value="submit">
        </form>""")
      
go="""
  <html>
    <body onload="window.location='http://127.0.1.1/test1.py'">
    </body>
  </html>
"""

a=form.getvalue('drop')
b=form.getvalue('preview')
if 'submit' in form  :
    fp=open("picture.jpg",'w')
    fp.write(form.getvalue('preview'))
    fp.close()
    """#cur.execute("drop table images")
    cur.execute("create table images(img blob)")
    cur.execute("insert into images values(?)",(buffer(form.getvalue('preview'),)))"""
    
    print("""
    <p><img src=""")
    data_uri = open('11.jpg', 'rb').read().encode('base64').replace('\n', '')
    img_tag = '<img src="data:image/jpg;base64,{0}">'.format(data_uri)
    print(img_tag)

    print("""alt="hii" style="width:320px;height:320px;border:0;"></p>
    </body>
    </html>
    """)
