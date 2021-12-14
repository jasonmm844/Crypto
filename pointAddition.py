# Jason Martin
# CS608
# December 12, 2021
# Found help from the following website
# https://asecuritysite.com/encryption/ecc_points_mult
import sys
import libnum

if len(sys.argv) < 8:
    print("Program usage: python* pointAddition.py <a value> <b value> <p value> <x1> <y1> <x2> <y2>\n")
    sys.exit(-1)

a=0
b=7
p=37
x1=6
x2=8

x1=int(sys.argv[4])
y1p=int(sys.argv[5])
x2=int(sys.argv[6])
y2p=int(sys.argv[7])
p=int(sys.argv[3])
a=int(sys.argv[1])
b=int(sys.argv[2])


print("a=",a)
print("b=",b)
print("p=",p)
print("x-point=",x1)
print("x-point=",x2)



# Get values of (x1,y1) and (x2,y1) to make sure they are on curve
z=(x1**3 + a*x1 + b) % p
if (libnum.has_sqrtmod(z,{p:1} )):
  y1=next(libnum.sqrtmod(z,{p:1}))
  if y1 != y1p:
      y1 = p - y1

z=(x2**3 + a*x2 + b) % p
if (libnum.has_sqrtmod(z,{p:1} )):
  y2=next(libnum.sqrtmod(z,{p:1}))
  if y2 != y2p:
      y2 = p - y2

print("\nP1\t(%d,%d)" % (x1,y1))
print("P2\t(%d,%d)" % (x2,y2))


# Add Points (x1,y1) + (x2,y2) = (x3,y3)
s=(y2-y1) *  libnum.invmod(x2-x1,p)
x3=(s**2-x2-x1) % p
y3=((s*(x2-x3)-y2)) % p

print("P1+P2\t(%d,%d)" % (x3,y3))
