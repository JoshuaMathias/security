import hashlib
import string
import random
import time
import sys
from itertools import permutations

def id_generator(size=6, chars=string.letters+string.digits):
    return ''.join(random.choice(chars) for _ in range(size))


option=sys.argv[1]
length=int(sys.argv[2])
chars=string.letters+string.digits
if (option=='collision'):
    start=time.time()
    secondList=[]
    firstList={}
    for i in range(len(chars)):
        if time.time()-start>10:
            break
        options=[''.join(p) for p in permutations(chars,i)]
        for opt in options:
            if time.time()-start>10:
                break
            nextHash=hashlib.sha1(opt).hexdigest()[0:length]
            if nextHash in firstList:
                print str(time.time()-start)+" Found collision. Both string "+opt+ " and "+firstList[nextHash]+" have hash "+nextHash+"."
                break
            else:
                firstList[nextHash]=opt
# pre-image attack
else:
    start=time.time()
    givenHash=hashlib.sha1(id_generator()).hexdigest()[0:length]
    print "Original hash: "+givenHash
    for i in range(len(chars)):
        if time.time()-start>20:
            break
        # print "Trying strings of length "+str(i)
        options=[''.join(p) for p in permutations(chars,i)]
        for opt in options:
            if time.time()-start>20:
                break
            nextHash=hashlib.sha1(opt).hexdigest()[0:length]
            if nextHash == givenHash:
                print str(time.time()-start)+" Found string with same hash: "+opt
                break
