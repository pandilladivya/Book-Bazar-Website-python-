#!/usr/bin/env python
import cgi, os
import cgitb; cgitb.enable()

try: # Windows needs stdio set for binary mode.
    import msvcrt
    msvcrt.setmode (0, os.O_BINARY) # stdin  = 0
    msvcrt.setmode (1, os.O_BINARY) # stdout = 1
except ImportError:
    pass

form = cgi.FieldStorage()

print("Content-Type:html/text\n\n")
print("""<html><body>
<form enctype="multipart/form-data" method="post">
<p>File: <input type="file" name="file"></p>
<p><input type="submit" name="submit" value="Upload"></p>
</form>
</body></html>""")







# Test if the file was uploaded
if 'submit' in form:

   # A nested FieldStorage instance holds the file
   fileitem = form.getvalue('file')
   
   
else:
   message = 'No file was uploaded'
   
print("""
<html><body>
<p>%s</p>
</body></html>
""" % (message,))
