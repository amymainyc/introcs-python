X = [901,4,246,4,2,6,85,245,5,5,4]

def sumdigits(n):
    n = str(n)
    if n == '':
        return 0
    else:
        return int(sumdigits(n[:-1])) + int(n[-1])

def biggest(L):
    if len(L) < 2:
        return L
    elif int(L[-2]) > int(L[-1]):
        L.remove(L[-1])
        return biggest(L)
    else:
        L.remove(L[-2])
        return biggest(L)
    
def ten2two(n):
    
def baseConvert(n,inbase,outbase):