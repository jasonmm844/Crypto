# Jason Martin
# CS608
# December 12, 2021
# Found help from the following website
# https://asecuritysite.com/encryption/ecc_points_mult

import sys
import libnum

if len(sys.argv) < 4:
    print("Program Usage: python* findOrderEC.py <a value> <b value> <p value>")
    sys.exit(-1)

a = int(sys.argv[1])
b = int(sys.argv[2])
p = int(sys.argv[3])
x = 0
n = 2 * p

highestOrder = 0
highestX = 0
highestY = 0

while x < p:


    z=(x**3 + a*x +b) % p
    if (libnum.has_sqrtmod(z,{p:1} )):
      y=next(libnum.sqrtmod(z,{p:1}))
    else:
        #print(x,"has no point on curve.\n")
        x = x + 1
        continue


    print("Checking Point: (%d,%d)" % (x,y))

    if ((y**2 % p) != ((x**3+a*x+b) %p)):
        print("  \tPoint is not on curve")
        x = x + 1
        continue

    s=((3*x**2)+a) * libnum.invmod(2*y,p)
    x1=(s**2-2*x) % p
    y1=((s*(x-x1))-y) % p

    x3=x1
    y3=y1
    x2=0
    y2=0
    counter=1

    for i in range(2, n+1):
        counter=counter+1
        if (counter>n):
            sys.exit()

        #print("%dP\t(%d,%d)" % (counter,x1,y1), end=' ')
    #    if ((y1**2 % p) == ((x1**3+a*x1+b) %p)):
    #        print("  \tPoint is on curve")

        if x1 == x:
            print("Order of point",x,"is:",counter+1,"\n")
            if counter+1 > highestOrder:
                highestOrder = counter+1
                highestX = x
                highestY = y
            break
        else:
            rtn=libnum.invmod(x1-x,p)


        if (rtn==0):
            print("%dP=0" % (counter+1))
            counter=counter+2
            s=((3*x**2)+a) *  libnum.invmod(2*y,p)

            x1=(s**2-2*x) % p

            y1=((s*(x-x1))-y) % p
            print("%dP\t(%d,%d)" % (counter,x,y), end=' ')
            if ((y**2 % p) == ((x**3+a*x+b) %p)): print("  \tPoint is on curve")


        else:
            s=(y1-y)* rtn

            x2=(s**2-x1-x) % p

            y2=((s*(x1-x2)-y1)) % p

            x1=x2
            y1=y2
    x = x + 1


print("Highest Order:",highestOrder,"at point(" + str(highestX) + "," + str(highestY) + ")")
