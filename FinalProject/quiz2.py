#! /usr/bin/python3

print ('Content-type: text/html\n')


Template='''<!DOCTYPE html>
<html>
<head>
<title>Quiz 2 Results</title>

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
    <img src="https://i.imgur.com/Om41C1U.gif" alt="a">
    <br><br>
    Incorrect answers:
    ???incorrect???
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
    if q1a.lower() == 'utah':
        score += 1
    else:
        wrong += '<br>1. Arches National Park in Utah'
    q2a=form.getvalue('q2','')
    if q2a.lower() == 'florida':
        score += 1
    else:
        wrong += '<br>2. Disneyworld in Florida'
    q3a=form.getvalue('q3','')
    if q3a.lower() == 'new york':
        score += 1
    else:
        wrong += '<br>3. Time Square in New York'
    q4a=form.getvalue('q4','')
    if q4a.lower() == 'wyoming':
        score += 1
    else:
        wrong += '<br>4. Old Faithful Geyser in Wyoming'
    q5a=form.getvalue('q5','')
    if q5a.lower() == 'alaska':
        score += 1
    else:
        wrong += '<br>5. Denali Mountain in Alaska'
    q6a=form.getvalue('q6','')
    if q6a.lower() == 'south dakota':
        score += 1
    else:
        wrong += '<br>6. Mount Rushmore in South Dakota'
    q7a=form.getvalue('q7','')
    if q7a.lower() == 'missouri':
        score += 1
    else:
        wrong += '<br>7. Gateway Arch in Missouri'
    q8a=form.getvalue('q8','')
    if q8a.lower() == 'hawaii':
        score += 1
    else:
        wrong += '<br>8. Pearl Harbor Memorial in Hawaii'
    q9a=form.getvalue('q9','')
    if q9a.lower() == 'arizona':
        score += 1
    else:
        wrong += '<br>9. Grand Canyon National Park in Arizona'
    q10a=form.getvalue('q10','')
    if q10a.lower() == 'washington':
        score += 1
    else:
        wrong += '<br>10. Space Needle in Washington'
    q11a=form.getvalue('q11','')
    if q11a.lower() == 'california':
        score += 1
    else:
        wrong += '<br>11. Golden Gate Bridge in California'
    q12a=form.getvalue('q12','')
    if q12a.lower() == 'illinois':
        score += 1
    else:
        wrong += '<br>12. Cloud Gate in Illinois'
    q13a=form.getvalue('q13','')
    if q13a.lower() == 'nevada':
        score += 1
    else:
        wrong += '<br>13. Las Vegas in Nevada'
    q14a=form.getvalue('q14','')
    if q14a.lower() == 'new york':
        score += 1
    else:
        wrong += '<br>14. Statue of Liberty in New York'
    q15a=form.getvalue('q15','')
    if q15a.lower() == 'arizona' or q15a.lower() == 'nevada':
        score += 1
    else:
        wrong += '<br>15. Hoover Dam in Arizona/Nevada'
    
    
    #calculate score
    HTML=HTML.replace('???score???',str(score))
    
    #calculate percentage
    f=open('scores2.txt','r')
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
            f=open('scores2.txt','w')
            f.write(s1 + '\n' + str(score))
            f.close()
            #get percentage
            percent = round((len(s)-scores)/(len(s))*100)
            going = False
            
    HTML=HTML.replace('???percent???',str(percent)+'%')
    #which questions are wrong
    if len(wrong) > 0:
        HTML=HTML.replace('???incorrect???',wrong)
    else:
        HTML=HTML.replace('???incorrect???','none!')
        
    print (HTML)

main()
