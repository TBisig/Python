
    for x in range(1, 256):
        print x

#print1to255();

def printOdds():
    for x in xrange(1, 256, 2):
        print x

#printOdds();

def printIntsAndSums():
    sum = 0
    for x in range(0, 256):
        sum += x
        print x
        print sum

#printIntsAndSums();

def printArrayValues(arr):
    for x in arr:
        print(x)

#printArrayValues([1, 2, 3, 4])

def returnOddIntArr():
    arr = []
    for x in xrange(1, 256, 2):
        arr.append(x)

    return arr

#print(returnOddIntArr())

def squareArr(arr):
    for i, s in enumerate(arr):
        arr[i] = s * s

    return arr

#print squareArr([1,2,3])

def countGreaterThanY(arr, y):
    count = 0
    for x in arr:
        if x > y:
            count += 1
            print x
    return count

#print countGreaterThanY([1,2,3,4,5,6], 3)

def zeroNegatives(arr):
    for i, s in enumerate(arr):
        if(s < 0):
            arr[i] = 0
    return arr


#print zeroNegatives([1,2,-4,-5,0,5])

def printMaxMinAvg(arr):
    sum = 0
    max = arr[0]
    min = arr[0]
    for x in arr:
        if(max < x):
            max = x
        if(min > x):
            min = x
    sum += x    
    return [max, min, sum / len(arr)]

#print printMaxMinAvg([1,2,3,4,5,6])

def shiftLeft(arr):
    for i in range(0, len(arr) - 1):
        arr[i] = arr[i + 1]
    arr[-1] = 0
    return arr

print shiftLeft([1,2,3,4,5])

def swapForDojo(arr):
    for i, s in enumerate(arr):
        if(s < 0):
            arr[i] = 'Dojo'
    return arr

#print swapForDojo([0, 2, -4, 6, -1])
