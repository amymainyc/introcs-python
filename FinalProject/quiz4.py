#! /usr/bin/python3

print ('Content-type: text/html\n')


Template='''<!DOCTYPE html>
<html>
<head>
<title>Quiz 4 Results</title>

<style>

.container {
  display: inline-block;
  margin-top: 20px;
  margin-bottom: 20px;
  margin-right: 20px;
  margin-left: 20px;
  background-color: white;
  color: black;
  width: 680px;
}
body {
  background-color: #D3F0FF;
  text-align: center;
  color: white;
  font-family: Arial;
}
.buttonmain {
  background-color: #ffffff00;
  border: none;
  color: white;
  padding: 0px 0px;
  text-align: center;
  text-decoration: none;
  display: inline-block;
  font-size: 16px;
}

</style>
</head>
<body>


<br><br>
<a href="http://moe.stuy.edu/~amai20/stuyfeed/stuyfeed.html" class="buttonmain">
  <h1>STUYFEED</h1>
</a>

<br>
<div class="container" style="float:center">
  <br>
  <p style="font-family:'Courier New'">
    Your destination:
    <br>
    ???destination???
    <br><br>
    <img src="???image???" width="600" height="400">
    <br>
  </p>
  <br>
</div>

</body>
</html>
'''


import cgi, cgitb
cgitb.enable()
import random

def main():
    form=cgi.FieldStorage()
    
    HTML=Template
    S=0
    W=0
    D=0
    F=0
    
    #grading questions
    q1a=form.getvalue('q1','')
    if q1a == 'S':
        S += 1
    elif q1a == 'W':
        W += 1
    elif q1a == 'D':
        D += 1
    elif q1a == 'F':
        F += 1
    q2a=form.getvalue('q2','')
    if q2a == 'S':
        S += 1
    elif q2a == 'W':
        W += 1
    elif q2a == 'D':
        D += 1
    elif q2a == 'F':
        F += 1
    q3a=form.getvalue('q3','')
    if q3a == 'S':
        S += 1
    elif q3a == 'W':
        W += 1
    elif q3a == 'D':
        D += 1
    elif q3a == 'F':
        F += 1
    q4a=form.getvalue('q4','')
    if q4a == 'S':
        S += 1
    elif q4a == 'W':
        W += 1
    elif q4a == 'D':
        D += 1
    elif q4a == 'F':
        F += 1
    q5a=form.getvalue('q5','')
    if q5a == 'S':
        S += 1
    elif q5a == 'W':
        W += 1
    elif q5a == 'D':
        D += 1
    elif q5a == 'F':
        F += 1
    q6a=form.getvalue('q6','')
    if q6a == 'S':
        S += 1
    elif q6a == 'W':
        W += 1
    elif q6a == 'D':
        D += 1
    elif q6a == 'F':
        F += 1
    q7a=form.getvalue('q7','')
    if q7a == 'S':
        S += 1
    elif q7a == 'W':
        W += 1
    elif q7a == 'D':
        D += 1
    elif q7a == 'F':
        F += 1
    q8a=form.getvalue('q8','')
    if q8a == 'S':
        S += 1
    elif q8a == 'W':
        W += 1
    elif q8a == 'D':
        D += 1
    elif q8a == 'F':
        F += 1

    
    #calculate destination
    destination = ''
    image = ''
    
    if W == 8:
        destination = 'Jasper National Park, Alberta, CA'
        image = 'https://i.imgur.com/LJbzCOi.jpg'
    elif W == 7:
        destination = 'Jackson Hole, WY'
        image = 'https://i.imgur.com/1MuyOda.jpg'
    elif W == 6:
        destination = 'Denali National Park, AL'
        image = 'https://i.imgur.com/A61Dnbe.jpg'
    elif W == 5:
        destination = 'Quebec City, QC'
        image = 'https://i.imgur.com/32pxSOf.jpg'
        
    elif S == 8:
        destination = 'Aruba'
        image = 'https://i.imgur.com/T6pJBwn.jpg'
    elif S == 7:
        destination = 'Bora Bora, Tahiti'
        image = 'https://i.imgur.com/oH4ASkk.jpg'
    elif S == 6:
        destination = 'Maui, HI'
        image = 'https://i.imgur.com/InZ31Th.jpg'
    elif S == 5:
        destination = 'Oahu, HI'
        image = 'https://i.imgur.com/GZt8tYf.jpg'
        
    elif D == 8:
        destination = 'Grand Canyon National Park, AZ'
        image = 'https://i.imgur.com/gCZFUCh.jpg'
    elif D == 7:
        destination = 'Yellowstone National Park, WY'
        image = 'https://i.imgur.com/34KNFFw.jpg'
    elif D == 6:
        destination = 'Yosemite National Park, CA'
        image = 'https://i.imgur.com/lK33ZTy.png'
    elif D == 5:
        destination = 'Hawaii Volcanoes National Park'
        image = 'https://i.imgur.com/Q5tZmlr.jpg'
        
    elif F == 8:
        destination = 'Orlando, FL'
        image = 'https://i.imgur.com/mkAJKt7.jpg'
    elif F == 7:
        destination = 'Atlantis, Bahamas'
        image = 'https://i.imgur.com/f7Zvftg.jpg'
    elif F == 6:
        destination = 'Salt Lake City, Utah'
        image = 'https://i.imgur.com/0EUSjgE.jpg'
    elif F == 5:
        destination = 'San Francisco, CA'
        image = 'https://i.imgur.com/e8h34JC.jpg'
        
    elif S == 4:
        destination = 'San Diego, CA'
        image = 'https://i.imgur.com/sICbNSe.jpg'
    elif W == 4:
        destination = 'New York City, NY'
        image = 'https://i.imgur.com/s399bX4.jpg'
    elif D == 4:
        destination = 'White Sands National Monument, NM'
        image = 'https://i.imgur.com/yhDCwHD.jpg'
    elif F == 4:
        destination = 'Los Angeles, CA'
        image = 'https://i.imgur.com/6p0FZvf.jpg'
    
    else:
        Z = random.randint(1,4)
        
        if Z == 1:
            destination = 'Boston, MA'
            image = 'https://i.imgur.com/7fPMkln.jpg'
        elif Z == 2:
            destination = 'Chicago, IL'
            image = 'https://i.imgur.com/TEa9pb8.jpg'
        elif Z == 3:
            destination = 'Las Vegas, NV'
            image = 'https://i.imgur.com/21Uu9rH.jpg'
        elif Z == 4:
            destination = 'Monterey, CA'
            image = 'https://i.imgur.com/ASLw6HZ.jpg'
        
    


    HTML=HTML.replace('???destination???',destination)
    HTML=HTML.replace('???image???',image)
        
    print (HTML)

main()
