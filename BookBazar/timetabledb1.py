#!/usr/bin/env python3
import cgi
import sqlite3
path="/var/www/html/timetb.db"
con=sqlite3.connect(path)
cur=con.cursor()
def disp():
    print("enter this")
    #cur.execute("create table timetable(sub1 varchar(10),sub2 varchar(10),sub3 varchar(10),sub4 varchar(10),sub5 varchar(10),sub6 varchar(10),sub7 varchar(10),sub8 varchar(15))")
    #cur.execute("insert into timetable values('CO','Flat','SE','Dbms','Es','DLD','Dbms Lab','DLD Lab' );")
    
    cur.execute("select * from timetable");
    d=cur.fetchall()
    global a1
    global a2
    global a3
    global a4
    global a5
    global a6
    global a7
    global a8
    '''a1=d[0][0]
    a2=d[0][1]
    a3=d[0][2]
    a4=d[0][3]
    a5=d[0][4]
    a6=d[0][5]
    a7=d[0][6]
    a8=d[0][7]'''
    #print(a1,a2,a4,a8)
    try:
        cur.execute("insert into timetable values(?,?,?,?,?,?,?,? )",(a1,a2,a3,a4,a5,a6,a7,a8))
        con.commit()
    except Exception as e:
        print(e)
    
form = cgi.FieldStorage() 
print("Content-Type: text/html\n\n")

htmlFormat="""
<html>
    <body>
        <form>
            <table border="1">
            <tr>
               <td>Day</td> <td>9.30-10.20</td><td>10.20-11.10</td><td>11.25-12.15</td><td>12.15-1.05</td>
            </tr>
            <tr>
            <td>MON</td><td>{a1}</td><td>{a2}</td><td>{a3}</td><td>{a4}</td>
            </tr>
             <tr>
            <td>TUE</td><td></td>
            </tr>
             <tr>
            <td>WED</td><td></td>
            </tr>
            <tr>
            <td>THR</td><td></td>
            </tr>
            <tr>
            <td>FRI</td><td></td>
            </tr>
            <tr>
            <td>SAT</td><td></td>
            </tr>
            </table>
            <p></p>
            subject1:<input type="text" name="subj1" value=0></input></br>
            subject2:<input type="text" name="subj2" value=0></input></br>
            subject3:<input type="text" name="subj3" value=0></input></br>
            subject4:<input type="text" name="subj4" value=0></input></br>
            subject5:<input type="text" name="subj5" value=0></input></br>
            subject6:<input type="text" name="subj6" value=0></input></br>
            subject7:<input type="text" name="subj7" value=0></input></br>
            subject8:<input type="text" name="subj8" value=0></input></br>
            <input type="submit" name="submit1" value="Submit" />
        </form>
    </body>
</html>"""
a1=str(form.getvalue("subj1",0))
a2=str(form.getvalue("subj2",0))
a3=str(form.getvalue("subj3",0))
a4=str(form.getvalue("subj4",0))
a5=str(form.getvalue("subj5",0))
a6=str(form.getvalue("subj6",0))
a7=str(form.getvalue("subj7",0))
a8=str(form.getvalue("subj8",0))

if "submit1" in form:
    print("in func")
    disp()
print(htmlFormat.format(**locals()))
