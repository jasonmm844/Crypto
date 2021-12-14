# Jason Martin
# CS608
# December 12, 2021
# Found help from the following website
# https://asecuritysite.com/encryption/ecc_points_mult

import sys
import libnum

if len(sys.argv) < 5:
    print("Program Usage: python* findOrderEC.py <a value> <b value> <p value> <x>")
    sys.exit(-1)

a = int(sys.argv[1])
b = int(sys.argv[2])
p = int(sys.argv[3])
x = int(sys.argv[4])
n = 2 * p

# y^2 = x^3 + ax + b (mod p)
print("a=",a)
print("b=",b)
print("p=",p)
print("n=",n)
print("x-point=",x)


z=(x**3 + a*x +b) % p
if (libnum.has_sqrtmod(z,{p:1} )):
  y=next(libnum.sqrtmod(z,{p:1}))
else:
    print(x,"has no point on curve.")
    sys.exit()


print("P\t(%d,%d)" % (x,y), end=' ')

if ((y**2 % p) == ((x**3+a*x+b) %p)): print("  \tPoint is on curve")
else:
    print("  \tPoint is not on curve")
    sys.exit()

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
        sys.exit(0)
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
