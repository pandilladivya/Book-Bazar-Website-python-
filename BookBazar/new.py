#!/usr/bin/python
import cgi
form=cgi.FieldStorage()
print("Content-Type:text/html")
html="""
<html>
<body>
    <form>
        NUMBER1: <input type="text" name="a"/><br>
        NUMBER2: <input type="text" name="b"/><br>
        <input type="submit" name="submit"/><br>
        RESULT: {c}
    </form>
</body>
</html>"""
a1=form.getvalue("a",0)
a2=int(a1)
b1=form.getvalue("b",0)
b2=int(b1)
c=0
if "submit" in form:
    c=a2+b2
print(html.format(**locals()))
