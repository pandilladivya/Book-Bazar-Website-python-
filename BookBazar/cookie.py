#!/usr/bin/env python3.4
from http.cookies import*

# create the cookie
c=SimpleCookie();

# assign a value
c['usr']='passwor'
# set the xpires time
c['usr']['expires']=1*1*3*60
#print(c.js_output())
# print the header, starting with the cookie
print(c);
print("Content-type: text/html\n");

# empty lines so that the browser knows that the header is over
print("");
print("");
print(c.js_output())
# now we can send the page content
print("""
<html>
    <body>
        <h1>The cookie has been set</h1>
    </body>
</html>
""");

