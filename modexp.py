import math
import sys
import gmpy2
import binascii
import os

def modExp(x,exp,modValue):
    x=x%modValue
    result=1
    while exp>0:
        if (exp%2==1):
            result=(result*x)%modValue
        x=x**2%modValue
        exp=exp/2
    return result

if __name__ == "__main__":
    m=int(sys.argv[1])
    d=int(sys.argv[2])
    n=int(sys.argv[3])
    answer=modExp(m,d,n)
    print "Answer: "+str(answer)
    if modExp(modExp(m,65537,n),d,n)==m:
        print "It works"
    else:
        print "It doesn't work"
