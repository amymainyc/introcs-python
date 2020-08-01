#! /usr/bin/python
print('Content-type: text/html\n')

def RandomSchool():
    import random
    filename = 'SAT-2010.csv'
    
    f=open(filename)
    s=f.read()
    f.close()
    
    if '"' in s:
        pieces = s.split('"')
        s = ','.join(pieces)
    if ' ' in s:
        pieces = s.split(' ')
        s = ' '.join(pieces)
    
    schools = (s.split('\n'))
    schools = schools[1:]
    line = random.choice(schools)
    line = line.split(',')
    
    total = TotalScore(line)
    DBN = line[0]
    line = line[1:]
    writing = line[-1]
    math = line[-2]
    reading = line[-3]
    number = line[-4]
    schoolx = ','.join(line[:-4])
    school = ''
    
    for char in range(len(schoolx)):
        if char == 0:
            school += schoolx[char].upper()
        elif ord(schoolx[char-1]) == 32:
            school += schoolx[char].upper()
        else:
            school += schoolx[char].lower()
            
    return htmlify(DBN,school,number,reading,math,writing,total)


def TotalScore(line):
    try:
        result = int(line[-1]) + int(line[-2]) + int(line[-3])
    except:
        result = 's'
    return str(result)

    
def htmlify(DBN,school,numberoftests,reading,math,writing,total):
    result = '''<center><p class="auto-style1"><strong>Random School SAT Scores</strong></p></center>
<table style="width: 75%" border="1" align="center">
    <tr>
        <td>DBN</td>
        <td>School</td>
        <td>Number of tests</td>
        <td>Reading</td>
        <td>Math</td>
        <td>Writing</td>
        <td>Total</td>
    </tr>
    <tr>
        <td>''' + DBN + '''</td>
        <td >''' + school + '''</td>
        <td>''' + numberoftests + '''</td>
        <td>''' + reading + '''</td>
        <td>''' + math + '''</td>
        <td>''' + writing + '''</td>
        <td>''' + total + '''</td>
    </tr>
</table>
'''
    return result

print(RandomSchool())
    