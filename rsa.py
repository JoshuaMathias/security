import math
import sys
import gmpy2
import binascii
import os

def modExp(x,exp,modValue):
    if (exp==0):
        return 1
    newX=modExp(x,exp/2,modValue)
    if (exp%2==0):
        return newX**2%modValue
    else:
        return x*newX**2%modValue

def extendedGCD(a,b):
    s = 0
    old_s = 1
    t = 1
    old_t = 0
    r = b
    old_r = a
    while r != 0: 
        quotient = (old_r / r)
        # print "quotient: "+str(quotient)
        # print "original old_r: "+str(old_r)
        # print "quotient*r: "+str(quotient * r)
        (old_r, r) = (r, old_r - quotient * r)
        # print "old_r: "+str(old_r)
        # print "r: "+str(r)
        # prov=r
        # r=old_r-quotient*prov
        # old_r=prov

    print "greatest common divisor:"+ str(old_r)
    return old_r

def multInverse(a,n):
    t=0
    newT=1
    r=n
    newR=a

    while newR != 0: 
        quotient = (r / newR)
        (t, newT) = (newT, t-quotient*newT)
        (r, newR) = (newR, r-quotient*newR)
    if r>1:
        print "Numbers are not relatively prime"
        return
    if t<0:
        t+=n
    return t


if __name__ == "__main__":
    phi=65537
    numbersWork=False
    while not numbersWork:
        p=int(binascii.hexlify(os.urandom(63)),16)
        q=int(binascii.hexlify(os.urandom(63)),16)
        while gmpy2.is_prime(p)==False:
            p=int(binascii.hexlify(os.urandom(63)),16)
        while gmpy2.is_prime(q)==False:
            q=int(binascii.hexlify(os.urandom(63)),16)

        phi=(p-1)*(q-1)
        print "Trying phi(n)="+str(phi)
        if extendedGCD(phi,65537)==1:
            numbersWork=True
    print "p: "+str(p)
    print "q: "+str(q)
    n=p*q
    print "n: "+str(n)
    print "phi(n)="+str(phi)
    e=65537
    # d is the multiplicative inverse of e mod phi
    extendedGCD(e,phi)
    d=multInverse(e,phi)
    print "d: "+str(d)
    