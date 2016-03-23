#!/usr/bin/env python3
print("Content-Type:text/html")

home_again="""
<html>
  <link rel="stylesheet"  href="phomepage.css">
  <head>
   <header>
   <nav>
   <table width=100%>
   <tr>
      <br><br>
      <center><font size="7">BookBazaar</font><br></center>
      <p align=><marquee><font size="3">SHARE AND GAIN KNOWLEDGE WITH BookBazaar</font></marquee></p>
      </tr>
      <tr>
        <td bgcolor="orange">
           <h2><button type="button"><a href="abtus.py">About BookBazaar</a></button></h2>
        </td>
        <td bgcolor="orange">
         <h2><button type="button"><a href="contact.py">Contact Us</a></button></h2>
        </td>
      </tr>
     </table>
   </nav>
   </header>
 </head>
<body>
   <form method="get">
    <nav>
    <table width=100% height=70%>
         <tr>
           <td width=70%>
          <center> <img src="img1.png" alt="sorry ! pic not available .." ></center>
         </td>
         <td width=30%>
             <center>
             <marquee><font color=red> Inavlid hall ticket no. or password ....Try it again dude</marquee>  
              <fieldset>
                 <legend><italic><b>Login : </b></italic></legend>
                 <table>
                     <tr>
                        <td>
                         <b>hallticket no :</b>
                         </td>
                         <td>
                         <input type="text" name="hno">
                        </td
                     </tr>
                     <tr>
                        <td>
                         <b>password:</b>
                         </td>
                         <td>
                         <input type="password" name="password">
                        </td>
                     </tr>
                 </table>
                  <input type="submit" name="submit" value="Sign In">
                </fieldset>
                <marquee><h3>Not yet a member of BookBazar </h3></marquee><br>
                <button type="button"><a href="hno_verify.py">Register Now</a></button>
             </center>
          </td>
         </tr>
    </table>
    </nav>
   </form>
</body>
</html>
"""
print(home_again)        
    




