#0 1 2 3 4 5 6 7 8 9
#0 1 1 2 3 5 8 13 21 34

def fib(n):
    result = 0
    n1 = 0
    n2 = 1
    while n != 0:
        result = n1 + n2
        n2 = n1
        n1 = result
        n = n - 1
        try: print (result/n2)
        except: pass
        
def fib_r(n):
    if n < 2:
        return n
    return fib_r(n-1) + fib_r(n-2)

def timit(n):
    import time
    start = time.time()
    fib_r(n)
    end = time.time()
    return(end - start)

def CalcFibRatios(low,high):
    for i in range(low,high+1):
        print(timit(i)/timit(i-1))
        
def fib_r2(n):
    fib_r2_helper(0,1,1,n)
    
def fib_r2_helper(prev,curr,pos,target):
    if pos==target:
        return curr
    her_target = target
    her_curr = prev + curr
    her_prev = curr
    her_pos = pos + 1
    
    return fib_r2_helper(her_prev,her_curr,her_pos,her_target)    