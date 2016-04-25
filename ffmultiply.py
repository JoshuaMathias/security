import sys
import operator

def xtime(p):
    #real implementations make a 256 byte table out of this

    p = p << 1
    # print bin(p)
    if (p & 0x100):
        p = p ^ 0x11b
    return p

def ff_mult(x, y):
    #following the steps from the example in the paper

    #build xtime table
    tab = [x]
    for i in range(7):
        tab.append(xtime(tab[i]))

    #find terms
    terms = []
    for i in range(7):
        if (0x1 << i & y):
            terms.append(tab[i])

    #sum them

    #out = 0x0
    #for i in terms:
    #   out = out ^ i

    out = reduce(operator.xor, terms)

    return out

def ff_mult2(x, y):
    #all in one loop
    out = 0x0
    curr = x
    for i in range(7):
        if(0x1 << i & y):
            out = out ^ curr
        curr = xtime(curr)
    return out


def main():
    # print sys.argv[1] + " "+sys.argv[2]
    answer=hex(ff_mult(0x28,0xdf))
    print str(answer)+" in binary: "
    print hex(ff_mult2(0xd4,0x2)^ff_mult2(0xbf,0x3)^0x5d^0x30)
    # print hex(ff_mult2(int(sys.argv[1]),int(sys.argv[2]))^ff_mult2(3,191)^93^48)
    # db 13 53 45
    # print hex(ff_mult2(0xdb,0x2)^ff_mult2(0x13,0x3)^0x53^0x45)
    # print hex(ff_mult2(0x2,0xdb)^ff_mult2(0x3,0x13)^0x53^0x45)

    # print hex(xtime(int(sys.argv[1],16)))

if __name__ == '__main__':
  main()

