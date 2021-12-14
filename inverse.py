# Jason Martin
    # CS608-001 Crpytography
        # Midterm Exam Program
            # October 27, 2021

import sys

if len(sys.argv) < 3:
        print("program usage: python* inverse.py [-v] <any positive integer> <any positive integer>\n")
        sys.exit()

verbose = False
if len(sys.argv) == 4:
    if sys.argv[1] != '-v':
        print("program usage: python* inverse.py [-v] <any positive integer> <any positive integer>\n")
        sys.exit()
    else:
        verbose = True
        a = int(sys.argv[2])
        p = int(sys.argv[3])
else:
    a = int(sys.argv[1])
    p = int(sys.argv[2])

if a > p:
    a = a % p

quotients = {}

count = 1
t = p
b = a
f = 0

while True:
    f = t // b
    h = t - f * b
    quotients[count] = f
    if verbose:
        print(str(t) + " = " + str(b) + " * " + str(f) + " + " + str(h))
    t = b
    b = h
    if h == 1 or h == 0:
        break
    count = count + 1

if h == 0:
    print("GCD = " + str(t) + " and inverse does not exist.")
    sys.exit()


flag = count
t = 0
b = 1
while count > 0:
    h = f * b + t
    if verbose:
        print(str(h) + " = " + str(f) + " x " + str(b) + " + " + str(t))
    count = count - 1
    if count > 0:
        f = quotients[count]

    t = b
    b = h

# add one to account for offset
inverse = 0
flag = flag + 1
if (flag % 2) == 0:
    inverse = p - h
else:
    inverse = h
inverse = inverse % p
print("Inverse = " + str(inverse))
