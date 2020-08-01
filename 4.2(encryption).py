Julius_before='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
Julius_after='defghijklmnopqrstuvwxyzabcDEFGHIJKLMNOPQRSTUVWXYZABC'
X='John Smith'
Y='JOHN SmIth'
Z='Johns Myth'
W='Smith, John'
E='Brooks, Peter;Holmes, David;Pascu, Ms.;'
F='Zw z yrmv jvve wlikyvi zk zj sp jkreuzex fe kyv jyflcuvij fw Xzrekj'

# 1a. encrypt and decrypt julius text
def encrypt(s):
    result=''
    for x in s:
        if 87 < ord(x) < 91:
            result += chr(64 + (3 - (90 - ord(x))))
        elif 119 < ord(x) < 123:
            result += chr(96 + (3 - (122 - ord(x))))
        else:
            result += chr(ord(x) + 3)
    return result

def decrypt(s):
    result=''
    for x in s:
        if 64 < ord(x) < 68:
            result += chr(91 - (3 - (ord(x)-65)))
        elif 96 < ord(x) < 100:
            result += chr(123 - (3 - (ord(x)-97)))
        else:
            result += chr(ord(x) - 3)
    return result
    
# 1b. generalize encrypt/decrypt
def ShiftCrypt(some_text,shift):
    result=''
    for x in some_text:
        result += ShiftLetter(x,shift)
    return result

def ShiftLetter(c,n):
    negative=False
    if n<0:
        n = abs(n)
        negative=True
    if n > 26:
        n = n % 26
  
    if not (64 < ord(c) < 91 or 96 < ord(c) < 123):
        return c
    if (ord(c) < (91-n) or 96 < ord(c) < (123-n)) and negative==False:
        return chr(ord(c)+n)
    if ord(c) < 91 and negative==False:
        return chr(64+(n-(90-ord(c))))
    if ord(c) < 123 and negative==False:
        return chr(96+(n-(122-ord(c))))
    
    if negative == True:
        n = 0-n
    if (64-n < ord(c) < 91) or (96-n < ord(c) < 123):
        return chr(ord(c)+n)
    if ord(c) < 91:
        return chr(90-(abs(n)-(ord(c)-64)))
    else:
        return chr(122-(abs(n)-(ord(c)-96)))
    
# 2a. two names are same?
def IsSameName(name1,name2):
    final1=name1.lower()
    final2=name2.lower()
    return final1==final2

#2b. capitalize words
def CapWord(word):
    result=''
    for x in range(len(word)):
        if x==0:
            a=word[0]
            result += a.upper()
        else:
            b=word[x]
            result += b.lower()
    return result

#2c. capitalize names
def CapName(name):
    result=''
    for x in range(len(name)):
        if x==0:
            a=name[0]
            result += a.upper()
        elif ord(name[x-1])==32:
            b=name[x]
            result += b.upper()
        else:
            c=name[x]
            result += c.lower()
    return result

#3a. change names to last name, first
def FirstLast(name):
    a= name.split(', ')
    return a[1]+' '+a[0]

#3b. 3a but with multiple names separated by ;
def FirstLastSequence(names):
    result=''
    names=names[:-1]
    x= names.split(';')
    for person in x:
        result += FirstLast(person)+';'
    return result

#4. classify files
def FileClassifier(filename):
    filename=filename.lower()
    for x in range(len(filename)):
        if ord(filename[x])==46:
            period=x
    filetype=filename[period:]
    
    if filetype == '.jpg':
        filetype = 'picture'
    elif filetype == '.jpeg':
        filetype = 'picture'
    elif filetype =='.nlogo':
        filetype = 'Netlogo'
    elif filetype =='.py':
        filetype = 'Python'
    elif filetype =='.mp3':
        filetype = 'music'
    return filetype
    
#Challenge:
def TCP(s):
    for x in range(26):
        result = ShiftCrypt(s,x)
        if result.find('Knick') > -1:
            return result
        elif result.find('Net') > -1:
            return result
        elif result.find('Met') > -1:
            return result
        elif result.find('Jet') > -1:
            return result
        elif result.find('Yankee') > -1:
            return result
        elif result.find('Ranger') > -1:
            return result
        elif result.find('Giant') > -1:
            return result
        
        