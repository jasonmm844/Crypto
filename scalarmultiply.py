# Jason Martin
# CS608
# December 12, 2021
# Found help from the following website
# https://asecuritysite.com/encryption/ecc_points_mult

import sys
import libnum

def scalarmultiply(a,b,p,n,x,ypt):
    z=(x**3 + a*x +b) % p
    if (libnum.has_sqrtmod(z,{p:1} )):
      y=next(libnum.sqrtmod(z,{p:1}))
      if ypt != y:
          y = p - y

    print("P\t(%d,%d)" % (x,y), end=' ')

    if ((y**2 % p) == ((x**3+a*x+b) %p)):
        print("  \tPoint is on curve")
    else:
        print("  \tPoint is not on curve")
        sys.exit()

    # Perform 2P or P+P
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
        if (counter>n): sys.exit()

        print("%dP\t(%d,%d)" % (counter,x1,y1), end=' ')
        if ((y1**2 % p) == ((x1**3+a*x1+b) %p)): print("  \tPoint is on curve")

        if x1 == x:
            print("Order of point is:",counter+1)
            return counter+1
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


if len(sys.argv) < 7:
    print("Program Usage: python* scalarmultiply.py <a value> <b value> <p value> <scalar value> <x> <y>")
    sys.exit(-1)

a = int(sys.argv[1])
b = int(sys.argv[2])
p = int(sys.argv[3])
n = int(sys.argv[4])
x = int(sys.argv[5])
ypt = int(sys.argv[6])

# y^2 = x^3 + ax + b (mod p)
print("a=",a)
print("b=",b)
print("p=",p)
print("n=",n)
print("x-point=",x)
print("y-point=",ypt)

order = scalarmultiply(a,b,p,n,x,ypt)

if order < n:
    scalarmultiply(a,b,p,n % order,x,ypt)
