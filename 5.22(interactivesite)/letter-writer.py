#! /usr/bin/python3

print ('Content-type: text/html\n')

Template='''<!DOCTYPE html>
<html>
<body>
???date???
<br><br>
Dear ???gender??? ???lname???,
<br><br>
It is with great pleasure that we have decided to send you this ???item??? as a small token of our esteem.
<br><br>
Unfortunately, returns are currently not possible.
<br>
Sincerely,
<br>
The Management
<br><br>
'''


import cgi, cgitb
cgitb.enable()

def main():
    form=cgi.FieldStorage()
    
    HTML=Template

    if form.getvalue('date','')=='ON':
        date='Monday, 3rd month, 12 B.C.E.'
    else:
        date=''
    HTML=HTML.replace('???date???',date)
    
    gender=form.getvalue('gender','')
    HTML=HTML.replace('???gender???',gender)

    lname=form.getvalue('lname','')
    HTML=HTML.replace('???lname???',lname)
    
    item=form.getvalue('item','')
    HTML=HTML.replace('???item???',item)

    print (HTML)

def exe():
    try: main()
    except: print('Error: Please fill in all fields.')
    
exe()
