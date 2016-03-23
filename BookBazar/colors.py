#!/usr/bin/env python
import cgi
form=cgi.FieldStorage()

colors=form.getlist('color')

print("Content-Type:text/html\n\n")

html="""
<html>
<body>
<form method="get" action="process_check.py">
<input type="submit" value="Submit">
</form>
</body>
</html>
"""
html1="""
<html>
<form  method="get">
Red:<input type="text" name ="color" value="red"></br>
Green:<input type="text" name="color" value="green"></br>
<input type="submit" value="Submit">
</form></html>
"""
print(html1)
lst=[]
i=0
for color in colors:
    lst.append(color)
    print("\n")
    print(lst[i],"\n")
    if(lst[i]=="green"):
        html1=html
        print("Click submit to go to next page")
        print(html1)
    i=i+1
