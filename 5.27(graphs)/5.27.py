import matplotlib.pyplot as plt
import random

data = [random.randrange(0,100) for num in range(100000)]

def Histo10():
    fig, ax = plt.subplots()
    plt.hist(data)
    ax.set_ylabel('Number of occurances')
    ax.set_xlabel('Numbers')
    ax.set_title('100,000 Random Numbers Between 0-99')
    xt = list(range(0,100,10))
    plt.xticks(xt)
    plt.savefig('histo10.png')
    plt.show()
    return ''

def Histo100():
    fig, ax = plt.subplots()
    plt.hist(data,bins=100)
    ax.set_ylabel('Number of occurances')
    ax.set_xlabel('Numbers')
    ax.set_title('100,000 Random Numbers Between 0-99')
    xt = list(range(0,100,5))
    plt.xticks(xt)
    plt.savefig('histo100.png')
    plt.show()
    return ''

def Popbar():
    f = open('townpop.csv')
    info = f.read()
    f.close()
    
    pop = []
    info = info.split('\n')
    
    for item in range(len(info)):
        things = info[item].split(',')
        if item == 0:
            pass
        else:
            try: pop.insert(0,things[-1][0])
            except: pass
    
    pop.sort()
            
    fig, ax = plt.subplots()
    plt.hist(pop,bins=10)
    ax.set_ylabel('Number of towns')
    ax.set_xlabel('First Digit of Population')
    ax.set_title('Town Populations')
    xt = list(range(0,10,1))
    plt.xticks(xt)
    plt.savefig('popbar.png')
    plt.show()
            
    return ''
