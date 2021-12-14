# Jason Martin
    # CS608-001 Crpytography
        # Midterm Exam Program
            # October 27, 2021

import sys

if len(sys.argv) < 2:
        print("program usage: python* generator.py [-v] <any positive integer>\n")
        sys.exit()

p = 0

if len(sys.argv) == 3 and sys.argv[1] == '-v':
    p = int(sys.argv[2])
elif len(sys.argv) == 2 :
    p = int(sys.argv[1])
else:
    print("program usage: python* generator.py [-v] <any positive integer>\n")
    sys.exit()

g = 4
flag = 0

while g < p:
    i = 1
    while i < p:
        print(g)
        if (g ** (p-1)) % p != 1:
            break
        x = (g ** i) % p
        if x == 1 and i != p - 1:
            break
        elif x == 1 and i == p - 1:
            flag = 1
        i = i + 1
    if flag == 1:
        break
    else:
        g = g + 1

if len(sys.argv) == 3 and sys.argv[1] == '-v':
    i = 1
    while i < p:
        print(str(g) + "^" + str(i) + " = " + str(g**i % p) + " (mod " + str(p) + ")")
        i = i + 1

print("Generator for " + str(p) + " is " + str(g))
