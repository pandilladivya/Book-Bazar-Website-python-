#!/usr/bin/env python3
import os
import cgi
from http.cookies import*
import cgi, os

  
if 'HTTP_COOKIE' in os.environ:
    string_cookie=os.environ.get('HTTP_COOKIE')
    c=SimpleCookie()
    c.load(string_cookie)
    for i in c:
        c[i]['expires']=0*0*0*0
    #print(c)


os.system('/var/www/html/homePage.py')

