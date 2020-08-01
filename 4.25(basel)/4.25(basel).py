import sys
import math

def basel(numbers):
    result = '''<html>
<body>
<center>
<h3>The Basel Problem Calculations</h3>
<table border="1">
<tr><b>
<td>N</td><td>Sum</td><td>pi*pi/6</td><td>Difference</td></b></tr>
'''
    for x in range(len(numbers)):
        if x < 2:
            pass
        elif numbers[x].isdigit() == False:
            return '''Correct usage: python basel.py filename num [num ...]
Must have one or more positive integers'''
        else:
            result += eachbasel(numbers[x]) + '''
'''
    result += '''</table>
</center>
</body>

</html>
'''
    writefile(sys.argv[1], result)
    
def eachbasel(number):
    n = float(number)
    summ = 0.0
    pi = (math.pi**2)/6
    while n != 0:
        summ = summ + (1/(n*n))
        n = n - 1
        
    return '<tr><td>' + str(number) + '</td><td>' + str(summ) + '</td><td>' + str(pi) + '</td><td>' + str(pi-summ) + '</td></tr>'

def writefile(filename,data):
    try: 
        f = open(filename, 'w')
        f.write(data)
        f.close
    except:
        print('''Correct usage: python basel.py filename num [num ...]
Cannot write in requested file''')
    

basel(sys.argv)
