#!/usr/bin/env python3.4
import os
from http.cookies import*
import cgitb
cgitb.enable()

print("Content-type: text/html\r\n\n")
print("in rcookie")
print("");
print("""
<html>
<body>
<h1>Check the cookie</h1>
""");
print(os.environ);
if 'HTTP_COOKIE' in os.environ:
 print("hi")
 cookie_string=os.environ.get('HTTP_COOKIE')
 c=SimpleCookie()
 c.load(cookie_string)

 try:
  data=c['usr'].value;
  print("cookie data: "+data+"<br>");
 except:
  print("The cookie was not set or has expired<br>");
  cgitb.handler();
         

print("""
</body>
</html>

""");

