L = 'randomNums.txt'
H = 'hamlet.txt'

def MinMaxList(filename):
    f = open(filename,'r')
    s = f.read()
    s = s.split('\n')
    
    d = {}
    
    for anum in s:
        if anum in d:
            d[anum] += 1
        else:
            d[anum] = 1
            
    most = ''
    mostnum = 0
    
    for item in d:
        if d[item] > mostnum:
            most = item
            mostnum = d[item]
            leastnum = d[item]
            
    least = ''
    
    for item in d:
        if d[item] < leastnum:
            least = item
            leastnum = d[item]

    print('Max number ' + most + ' appears ' + str(mostnum) + ''' times
''' + 'Min number ' + least + ' appears ' + str(leastnum) + ' time')
    
def hamlet(filename):
    f = open(filename,'r')
    s = f.read()
    
    s = s.split('\n')
    s = ''.join(s)
    s = s.lower()
    
    d = {}
    
    for letter in s:
        if ord(letter) > 127:
            pass
        elif letter in d:
            d[letter] += 1
        else:
            d[letter] = 1
    
    most = ''
    mostnum = 0
    second = ''
    secondnum = 0
    third = ''
    thirdnum = 0
    
    for item in d:
        if d[item] > mostnum:
            third = second
            thirdnum = secondnum
            second = most
            secondnum = mostnum
            most = item
            mostnum = d[item]
        elif d[item] > secondnum:
            third = second
            thirdnum = secondnum
            second = item
            secondnum = d[item]
        elif d[item] > thirdnum:
            third = item
            thirdnum = d[item]
            
    
    leastnum = mostnum        
    least = ''
    
    secondl = ''
    secondlnum = 0
    thirdl = ''
    thirdlnum = 0
    
    for item in d:
        if d[item] < leastnum:
            thirdl = secondl
            thirdlnum = secondlnum
            secondl = least
            secondlnum = leastnum
            least = item
            leastnum = d[item]
        elif d[item] < secondlnum:
            thirdl = secondl
            thirdlnum = secondlnum
            secondl = item
            secondlnum = d[item]
        elif d[item] < thirdlnum:
            thirdl = item
            thirdlnum = d[item]
    
    print('most frequent characters:' + '''
''' + most + ' ' + str(mostnum) + '''
''' + second + ' ' + str(secondnum) + '''
''' + third + ' ' + str(thirdnum) + '''
'''
'least frequent characters:' + '''
''' + least + ' ' + str(leastnum) + '''
''' + secondl + ' ' + str(secondlnum) + '''
''' + thirdl + ' ' + str(thirdlnum)
          )
    
def hamlet2(filename):
    f = open(filename,'r')
    s = f.read()
    
    s = s.split('\n')
    s = ' '.join(s)
    s = s.lower()
    
    for char in s:
        if 96 < ord(char) < 123:
            pass
        elif ord(char) == 32:
            pass
        else:
            s = s.split(char)
            s = ''.join(s)

    d = {}
    s = s.split(' ')
    
    for word in s:
        if word == '':
            pass
        elif word in d:
            d[word] += 1
        else:
            d[word] = 1
            
    most = ''
    mostnum = 0
    second = ''
    secondnum = 0
    third = ''
    thirdnum = 0
    fourth = ''
    fourthnum = 0
    fifth = ''
    fifthnum = 0
    
    for item in d:
        if d[item] > mostnum:
            fifth = fourth
            fifthnum = fourthnum
            fourth = third
            fourthnum = thirdnum
            third = second
            thirdnum = secondnum
            second = most
            secondnum = mostnum
            most = item
            mostnum = d[item]
        elif d[item] > secondnum:
            fifth = fourth
            fifthnum = fourthnum
            fourth = third
            fourthnum = thirdnum
            third = second
            thirdnum = secondnum
            second = item
            secondnum = d[item]
        elif d[item] > thirdnum:
            fifth = fourth
            fifthnum = fourthnum
            fourth = third
            fourthnum = thirdnum
            third = item
            thirdnum = d[item]
        elif d[item] > fourthnum:
            fifth = fourth
            fifthnum = fourthnum
            fourth = item
            fourthnum = d[item]
        elif d[item] > fifthnum:
            fifth = item
            fifthnum = d[item]
            
    print('most frequent words:' + '''
''' + most + ' ' + str(mostnum) + '''
''' + second + ' ' + str(secondnum) + '''
''' + third + ' ' + str(thirdnum) + '''
''' + fourth + ' ' + str(fourthnum) + '''
''' + fifth + ' ' + str(fifthnum)
        )