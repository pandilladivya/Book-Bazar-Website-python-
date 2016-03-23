#!/usr/bin/env python3
from http.cookies import*
import cgitb
cgitb.enable()
import cgi, os, sqlite3

path= '/var/www/html/bb.db'
con=sqlite3.connect(path)
cur=con.cursor()

print("Content-Type:text/html\n\n")

print("""<html>
        <link rel="stylesheet" type="text/css" href="test.css">
       <head>
          <ul id="menu">

            <li>
             <a href="index.html">About BookBazaar</a>
             <ul>
                 <li><a href="index.html">link1</a></li>
                 <li><a href="index.html">link2</a></li>
             </ul>
            </li>

             <li>
             <a href="index.html">contact us</a>
             <ul>
                 <li><a href="index.html">link1</a></li>
                 <li><a href="index.html">link2</a></li>
             </ul>
            </li>

            <li>
             <a href="index.html">logout</a>
             <ul>
                 <li><a href="index.html">link1</a></li>
                 <li><a href="index.html">link2</a></li>
             </ul>
            </li>
            
          </ul>
       </head>
       <body><br><br><br><br><br><br>
         <h1>ARE U DONE ??</h2>
       </body>
</html>
    """)
