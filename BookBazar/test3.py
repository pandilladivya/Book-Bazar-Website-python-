#!/usr/bin/env python3

import cgi, os
import cgitb; cgitb.enable()
import codecs
import sqlite3
path= '/var/www/html/bb.db'
con=sqlite3.connect(path)
cur=con.cursor()

print("Content-Type:text/html\n\n")


print("""
<html>
  <head><h1>hello this is title</h1></head>
  <body>
    is the image displayed ??
    <p><img src=""")
print("buy2.png")

print("""alt="hii" style="width:320px;height:320px;border:0;">
    <img src=""")
select="select * from images"
cur.execute(select)
i=cur.fetchall()
print(codecs.decode(i[3][0]))


print(""" alt="not working dude" style="width:320px;height:320px;border:0;"></p>
  </body>
</html>
""")






