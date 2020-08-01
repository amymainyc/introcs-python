#! /usr/bin/python3

print ('Content-type: text/html\n')


Template='''<!DOCTYPE html>
<html>
<head>
<title>Quiz 3 Results</title>

<style>

.container {
  display: inline-block;
  margin-top: 20px;
  margin-bottom: 20px;
  margin-right: 20px;
  margin-left: 20px;
  background-color: white;
  color: black;
  width: 400px;
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
    Your tastebuds are ???score??? years old.
    <br><br>
    Your tastebuds are older than <br>???percent??? of quiz takers!
    <br><br>
    <img src="https://i.imgur.com/c9GYULd.gif" alt="a" width="300" height="200">
    <br><br>
  </p>
  <br>
</div>



</body>
</html>
'''


import cgi, cgitb
cgitb.enable()

def main():
    form=cgi.FieldStorage()
    
    HTML=Template
    score=0
    wrong=''
    
    #grading questions
    q1a=form.getvalue('q1','')
    score += 60 - int(q1a)

    q2a=form.getvalue('q2','')
    score += int(q2a)
    
    q3a=form.getvalue('q3','')
    score += 60 - int(q3a)
    
    q4a=form.getvalue('q4','')
    score += int(q4a)
    
    q5a=form.getvalue('q5','')
    score += 60 - int(q5a)
    
    q6a=form.getvalue('q6','')
    score += int(q6a)
    
    q7a=form.getvalue('q7','')
    score += 60 - int(q7a)
    
    q8a=form.getvalue('q8','')
    score += int(q8a)
    
    q9a=form.getvalue('q9','')
    score += int(q9a)
        
    q10a=form.getvalue('q10','')
    score += 60 - int(q10a)
    
    q11a=form.getvalue('q11','')
    score += int(q11a)
    
    q12a=form.getvalue('q12','')
    score += int(q12a)
    
    q13a=form.getvalue('q13','')
    score += int(q13a)
    
    q14a=form.getvalue('q14','')
    score += int(q14a)
    
    q15a=form.getvalue('q15','')
    score += int(q15a)
    
    
    
    #calculate score
    score = round(score/15)
    HTML=HTML.replace('???score???',str(score))
    
    #calculate percentage
    f=open('scores3.txt','r')
    s=f.read()
    f.close()
    s = s.split('\n')
    
    #turn s into a number list
    a = [0,15]
    for number in s:
        try: a.insert(0, int(number))
        except: pass
    a = a[:-2]
    a.sort(reverse=True)

    
    going = True
    for scores in range(len(a)):
        if ((score == a[scores]) or score > int(a[scores])) and going == True:
            #write score in file
            s1 = '\n'.join(s)
            f=open('scores3.txt','w')
            f.write(s1 + '\n' + str(score))
            f.close()
            #get percentage
            percent = round((len(s)-scores)/(len(s))*100)
            going = False
            
    HTML=HTML.replace('???percent???',str(percent)+'%')
        
    print (HTML)

main()
