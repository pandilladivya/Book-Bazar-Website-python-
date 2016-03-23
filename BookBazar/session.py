#!/usr/bin/env python
try :
    import hashlib, time, http.cookies, os
    import cgi
    cookie = http.cookies.SimpleCookie()
    string_cookie = os.environ.get('HTTP_COOKIE')

    # If new session
    if not string_cookie:
       # The sid will be a hash of the server time
       t=hashlib.md5(repr(time.time()).encode())
       #t=hashlib.md5(b'hello world')
       sid=t.hexdigest()
       print(sid)
       #sid = sha.new(repr(time.time())).hexdigest()
       # Set the sid in the cookie
       cookie['sid'] = sid
       # Will expire in a year
       cookie['sid']['expires'] = 0 * 0 * 0 * 15 * 60
    # If already existent session
    else:
       cookie.load(string_cookie)
       sid = cookie['sid'].value

    """#print(cookie)
    print('Content-Type: text/html\n')
    print('<html><body>')

    if string_cookie:
       print('<p>Already existent session</p>')
    else:
       print('<p>New session</p>')

    print('<p>SID ={sid}</p>')
    print('</body></html>')
    """
    html="""
    <html>
     <body>
       this is the body 
     </body
    >
    </html>
    """
    print(html)
except Exception as e:
    print(e)
