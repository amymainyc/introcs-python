n='SAT-2010.csv'

def highlow(filename):
    f=open(filename)
    s=f.read()
    f.close()
    s=s.lower()
    
    if '"' in s:
        pieces = s.split('"')
        s = ','.join(pieces)
    if ' ' in s:
        pieces = s.split(' ')
        s = ' '.join(pieces)
    
    school=(s.split('\n'))
    highest=float(0)
    namehighest=''
    lowest=float(10000)
    namelowest=''
    
    for x in range(len(school)):
        items = school[x].split(',')
        score=0
        try: 
            score = score + int(items[-1]) + int(items[-2]) + int(items[-3])
        except:
            pass
        
        if x == 0:
            pass
        elif score == 0:
            pass
        elif float(score) > highest:
            highest = float(score)
            namehighest = items[1]
        elif float(score) < lowest:
            lowest = float(score)
            namelowest = items[1]
                
    
    answer=''''''
    
    for x in range(len(namehighest)):
        if x == 0:
            answer += str(namehighest[x].upper())
        elif ord(namehighest[x-1]) == 32:
            answer += str(namehighest[x].upper())
        else:
            answer += str(namehighest[x])
            
    answer += 'is highest with a score of ' + str(highest)[:-2] + '''
'''
    
    for y in range(len(namelowest)):
        if y == 0:
            answer += str(namelowest[y].upper())
        elif ord(namelowest[y-1]) == 32:
            answer += str(namelowest[y].upper())
        else:
            answer += str(namelowest[y])
            
    answer += 'is lowest with a score of ' + str(lowest)[:-2]
    
            
    return answer

def nthSchool(filename,whichscore,nth):
    f=open(filename)
    s=f.read()
    f.close()
    s=s.lower()
    
    if '"' in s:
        pieces = s.split('"')
        s = ','.join(pieces)
    if ' ' in s:
        pieces = s.split(' ')
        s = ' '.join(pieces)
    
    school=(s.split('\n'))
    
    #sort information into categories
    reading=''
    math=''
    writing=''
    
    for x in range(len(school)):
        items = school[x].split(',')
        if items[-1]=='s':
            pass
        elif x == 0:
            pass
        elif len(items) > 6:
            commaschool = items[2:-4]
            commaschool = ','.join(commaschool[:2])
            reading += items[-3] + '-' + commaschool + ';'
            math += items[-2] + '-' + commaschool + ';'
            writing += items[-1] + '-' + commaschool + ';'
        elif len(items) == 6:
            reading += items[-3] + '-' + items[1] + ';'
            math += items[-2] + '-' + items[1] + ';'
            writing += items[-1] + '-' + items[1] + ';'
            
    reading = reading.split(';')
    math = math.split(';')
    writing = writing.split(';')
            
    #order the info
    reading.sort(reverse=True)
    math.sort(reverse=True)
    writing.sort(reverse=True)
    
    reading =  reading[:-1]
    math = math[:-1]
    writing = writing[:-1]
    
    if whichscore == 'reading':
        answer = reading[nth]
    elif whichscore == 'math':
        answer = math[nth]
    elif whichscore == 'writing':
        answer = writing[nth]
        
    result = []
    for x in range(len(answer)):
        if x == 4:
            result += str(answer[x].upper())
        elif ord(answer[x-1]) == 32:
            result += str(answer[x].upper())
        else:
            result += str(answer[x])
    
    result = ''.join(result)
    result = result.split('-')
    result = ', '.join(result)
    result = result[:-1]
    return result


    
        
    
    
            
