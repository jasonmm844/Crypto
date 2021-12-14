# Jason Martin
    # CS608-001 Crpytography
        # Midterm Exam Program
            # October 27, 2021

import sys

if len(sys.argv) < 3:
        print("program usage: python* gcd.py [-v] <any positive integer> <any positive integer>\n")
        sys.exit()

a = 0
p = 0

verbose = False
if len(sys.argv) == 4:
    if sys.argv[1] != '-v':
        print("program usage: python* gcd.py [-v] <any positive integer> <any positive integer>\n")
        sys.exit()
    else:
        verbose = True
        a = int(sys.argv[2])
        p = int(sys.argv[3])
else:
    a = int(sys.argv[1])
    p = int(sys.argv[2])

count = 0
t = p
b = a



while True:
    f = t // b
    h = t - f * b
    if verbose:
        print(str(t) + " = " + str(b) + " * " + str(f) + " + " + str(h))
    t = b
    b = h
    if h == 1 or h == 0:
        break
    count = count + 1

if h == 1:
    print("GCD = 1 and inverse exists.")
elif h == 0:
    print("GCD = " + str(t))
