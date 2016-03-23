#!/usr/bin/env python3
import os
import cgi,cgitb
cgitb.enable()
from http.cookies import*
print("Content-Type:html/text\n\n")
print("""
<html>
<body background='/var/www/html/image_saver' >
</body>
</html>
""")
