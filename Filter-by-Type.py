def printInteger(x):
        if x >= 100:
            print "That's a big number!"
        else:
            print "That's a small number"

#printInteger(43); 

def sentence(str):
    if  len(str) >= 50:
        print "Long Sentence"
    else:
        print "Short Sentence"

#print sentence("jf;lasjasdkf;jaskdjf;laskjdf;skajdf;lksaj;dkfja;sldkjf;alksjdf;jas;djf;aslkdjf;ljkdf"); 

def printlist(list):
    if len(list) >= 10:
        print "Big list!"
    else:
        print "Short list"

printlist(['a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a'])
