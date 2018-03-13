# #input
l = ['magical unicorns',19,'hello',98.98,'world']
# #output
# "The list you entered is of mixed type"
# "String: magical unicorns hello world"
# "Sum: 117.98"
def checkType(l):
    sum = 0
    counter = 0 
    resultString = ""
    for el in l:
        if type(el) == int or type(el) == float:
            counter += 1
            sum += el
            print  "{}, this is an integer".format( el)
        if isinstance(el,str):
            print el
            resultString = "{} {}".format(resultString, el)
    if len(resultString) > 0 and counter > 0:
        print "mixed list"
    
    print "the current sum is : {}".format(sum)
    print "the final string is : {}".format(resultString)

checkType(l)
