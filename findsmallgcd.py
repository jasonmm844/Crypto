# Jason Martin
    # CS608-001 Crpytography
        # Midterm Exam Program
            # October 27, 2021

import sys

if len(sys.argv) < 2:
        print("program usage: python* findsmallgcd.py [-v] <any positive integer>\n")
        sys.exit()

p = 0

verbose = False
if len(sys.argv) == 3:
    if sys.argv[1] != '-v':
        print("program usage: python* findsmallgcd.py [-v] <any positive integer>\n")
        sys.exit()
    else:
        verbose = True
        p = int(sys.argv[2])
else:
    p = int(sys.argv[1])

count = 0
a = 2
while True:
    t = p
    b = a

    if verbose:
        print("\na = " + str(a))
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
        print("GCD = 1, e = " + str(a))
        break
    a = a + 1
