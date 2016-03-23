#!/usr/bin/env python3
import cgi
import os
from http.cookies import*
path='/var/www/html'
form=cgi.FieldStorage()
form_data=cgi.FieldStorage()
print("Content-Type:text/html\n\n")
print(
      """
    <html>
      <body>
       <form method="get">
        <select name="drop" >
          <option>5star</option>
          <option>Munch</option>
          <option>cadbury</option>
          <option>Kurkure</option>
        </select>
        <br>
         <input type="file" name="preview" accept="image/*" >
         <input type="submit" name="submit" value="submit">
        </form>
      </body>
    </html>
"""
    )
go="""
  <html>
    <body onload="window.location='http://127.0.1.1/test1.py'">
    </body>
  </html>
"""

a=form.getvalue('drop')
b=form.getvalue('preview')
if 'submit' in form and a!=None :
    name =  os.path.split(form['preview'].filename)
    file(name[-1], 'w').write(form['preview'].value)
