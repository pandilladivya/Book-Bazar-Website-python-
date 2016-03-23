def log(login):
 """login=[]
 login.append(form.getvalue('hno'))
 login.append(form.getvalue('password'))"""
 print(login)
 print(login[0])
 cur.execute("select hno,password from registered")
 data=cur.fetchall()
 for i in data:
    row=cur.fetchone()
    if(row[0]==login[0] and row[1]==login[1]):
        home=logged_in
        break
 else:
    print("login failed!!")
 print(home)




























     
