def print1to1000odds():
    for x in xrange(1, 1000, 2):
        print x

#print1to1000odds();

def printmultiplesof5():
    for x in xrange(0, 1000000, 5):
        print x;
    
#printmultiplesof5();

def printsumlist(arr):
    sum = 0
    for x in arr:
        sum += x
        print sum
    return sum

#printsumlist([1, 2, 5, 10, 255, 3]);

def printavg(arr):
    sum = 0
    for x in arr:
        sum += x
    print sum / len(arr)
    return [sum / len(arr)]

printavg([1, 2, 5, 10, 255, 3])