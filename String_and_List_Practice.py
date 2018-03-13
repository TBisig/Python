words = "It's Thanksgiving day. It's my birthday too!"
print words
print words.replace("day", "month")

def printMaxMin(arr):
    max = arr[0]
    min = arr[0]
    for x in arr:
        if(max < x):
            max = x
        if(min > x):
            min = x
    return [max , min]

print printMaxMin([2,54,-2,7,12,98])

def printFirstandLast(arr):
    first = arr[0]
    last = arr[-1]
    return [first , last]
print printFirstandLast(["hello",2,54,-2,7,12,98,"world"]);



