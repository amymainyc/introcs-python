n='salaries.csv'

def MaxSalary(filename):
    f=open(filename)
    s=f.read()
    f.close()
    
    person=(s.split('\n'))
    highest=float(0)
    namehighest=''
    
    for x in range(len(person)):
        items = person[x].split(',')
        if x == 0:
            highest = 0
        elif float(items[2]) > highest:
            highest = float(items[2])
            namehighest = items[0]
            
    return namehighest + ', ' + str(highest)
