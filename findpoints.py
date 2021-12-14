# Jason Martin
# CS608
# December 12, 2021
# Found help from the following website
# https://asecuritysite.com/encryption/ecc_points_real

import sys
import libnum



def findpoints(p,a,b):
    x=0
    count=0
    while True:
        val=((x*x*x) + a*x+ b) % p
        if (val==0):
          print (x,"0")
          count=count+1

        rtn= libnum.jacobi(val,p)

        if (rtn==1):
          res=next(libnum.sqrtmod(val,{p:1}))
          print("(",x,int(res),")",end='')
          print("(",x,int(p-res),")",end='')
          count=count+2
          if count % 10 == 0:
              print()
        x=x+1

        if (count>p*2 or x==p): return count

p=0
a=0
b=0

if len(sys.argv) < 4:
    print("Program usage: python* findpoints.py <a value> <b value> <p value>\n")
    sys.exit(-1)

a=int(sys.argv[1])
b=int(sys.argv[2])
p=int(sys.argv[3])


print ("Prime number:",p)
print ("a,b",a,b)

print ("y^2 = x^3 + ax +b (mod p)")
count=findpoints(p,a,b)
print ("\n\nOrder is ",count+1)
