def example():
    primes = [2,3,4,5,6]
    rainbow = ['red','orange', 'yellow','green','blue', 'indigo','violet']
    print(rainbow[0])               #print 0 element from the list
    rainbow[0] = 'красный'          #name 0 element as красный
    print('выведем радугу')
    for i in range(len(rainbow)):   #for a variable i in a range with length of rainbow,
        print(rainbow[i])           #print rainbow. It takes
    for a in range(len(primes)):
        print(primes[a])
example()

def toinen():
    my_list=['apple', 'orange', 'pear', 'rapsberry']
    print('Output')
    for c, value in enumerate(my_list,1):
        print(c,value)
toinen()

def kolmas():
    my_list = ['omena', 'banana', 'oranssi', 'salatti']
    counter_list = list(enumerate(my_list,1))
    print('Output')
    print(counter_list)
kolmas()

def neljas():
    a = tuple('hello,world')
    print(a)
neljas()

def viides():
    a=[1,2,3]
    b=list(a)
    print(a)
    print(b)
viides()

def kuudes():
    a=[]            #create an empty list
    a.append(3)     #add number 3
    a.append('hello')   #add hello to the list
    print(a)
kuudes()

def seitseman():
    b=[2,3,5]
    print(b)
    b.remove(3)
    print(b)
seitseman()

def kahdeksan():
    c=[1,2,3,4]
    c[2] = 17
    print(c)
kahdeksan()

def yhdeksan():
    a=[1,614,78,5,16]
    a.sort(key=None,reverse=True)
    print(a)
yhdeksan()
