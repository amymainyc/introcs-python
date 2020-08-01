#! /usr/bin/python3

print ('Content-type: text/html\n')


Template='''<!DOCTYPE html>
<html>
<head>
<title>Quiz 1 Results</title>

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
    Your score: ???score???/15
    <br><br>
    You did better than <br>???percent??? of quiz takers!
    <br><br>
    <img src="https://i.imgur.com/GyQmixp.gif" alt="a">
    <br><br>
    Incorrect answers: ???incorrect???
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
    if q1a == 'D':
        score += 1
    else:
        wrong += ', 1'
    q2a=form.getvalue('q2','')
    if q2a == 'A':
        score += 1
    else:
        wrong += ', 2'
    q3a=form.getvalue('q3','')
    if q3a == 'B':
        score += 1
    else:
        wrong += ', 3'
    q4a=form.getvalue('q4','')
    if q4a == 'A':
        score += 1
    else:
        wrong += ', 4'
    q5a=form.getvalue('q5','')
    if q5a == 'C':
        score += 1
    else:
        wrong += ', 5'
    q6a=form.getvalue('q6','')
    if q6a == 'B':
        score += 1
    else:
        wrong += ', 6'
    q7a=form.getvalue('q7','')
    if q7a == 'D':
        score += 1
    else:
        wrong += ', 7'
    q8a=form.getvalue('q8','')
    if q8a == 'C':
        score += 1
    else:
        wrong += ', 8'
    q9a=form.getvalue('q9','')
    if q9a == 'A':
        score += 1
    else:
        wrong += ', 9'
    q10a=form.getvalue('q10','')
    if q10a == 'A':
        score += 1
    else:
        wrong += ', 10'
    q11a=form.getvalue('q11','')
    if q11a == 'C':
        score += 1
    else:
        wrong += ', 11'
    q12a=form.getvalue('q12','')
    if q12a == 'B':
        score += 1
    else:
        wrong += ', 12'
    q13a=form.getvalue('q13','')
    if q13a == 'C':
        score += 1
    else:
        wrong += ', 13'
    q14a=form.getvalue('q14','')
    if q14a == 'B':
        score += 1
    else:
        wrong += ', 14'
    q15a=form.getvalue('q15','')
    if q15a == 'D':
        score += 1
    else:
        wrong += ', 15'
    
    
    #calculate score
    HTML=HTML.replace('???score???',str(score))
    
    #calculate percentage
    f=open('scores.txt','r')
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
            f=open('scores.txt','w')
            f.write(s1 + '\n' + str(score))
            f.close()
            #get percentage
            percent = round((len(s)-scores)/(len(s))*100)
            going = False
            
    HTML=HTML.replace('???percent???',str(percent)+'%')
    #which questions are wrong
    if len(wrong) > 0:
        HTML=HTML.replace('???incorrect???',wrong[2:])
    else:
        HTML=HTML.replace('???incorrect???','none!')
        
    print (HTML)

main()
