# Jason Martin
# CS608
# December 12, 2021

import sys
import libnum

if len(sys.argv) < 3:
    print("Program Usage: python* modsqrt.py <a value> <p value>")
    sys.exit(-1)

a = int(sys.argv[1])
p = int(sys.argv[2])

print("Finding square root for r^2 = ",a,"mod",p)

if ( libnum.has_sqrtmod(a,{p:1})):

    result = next(libnum.sqrtmod(a,{p:1}))

    print(int(result),"^ 2 = ",a,"mod",p)
    print(p - int(result),"^ 2 = ",a,"mod",p)

else:
    print("There is no square root for r^2 =",a,"mod",p)
