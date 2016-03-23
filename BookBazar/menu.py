#!/usr/bin/env python3
import os
import cgi
from http.cookies import*
form=cgi.FieldStorage()


import sqlite3
path= '/var/www/html/bb.db'
con=sqlite3.connect(path)
cur=con.cursor()
print("Content-Type:text/html\r\n\n")
print("")
print("")
print("""
<html>
<link rel="stylesheet"  href="phomepage.css">
<head>
  <ul id="menu">
     <li><a href="/var/www/html/homePage.py">Home</li>
     <li><a href="/var/www/html/abtus.py">About us</li>
     <li><a href="/var/www/html/contact.py">Home</li>
  </ul>
</head>
<body>
 <h1>Hello your page starts here ...</h1>
</body>
""")
