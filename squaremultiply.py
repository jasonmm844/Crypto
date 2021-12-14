# Jason Martin
    # CS608-001 Crpytography
        # Midterm Exam Program
            # October 27, 2021

import sys

if len(sys.argv) < 4:
        print("program usage: python* squaremultiply.py [-v] <base> <exponent> <modulo>\n")
        sys.exit()

b = 0
e = 0
m = 0
exponent = 0

verbose = False
if len(sys.argv) == 5:
    if sys.argv[1] != '-v':
        print("program usage: python* squaremultiply.py [-v] <base> <exponent> <modulo>\n")
        sys.exit()
    else:
        verbose = True
        b = int(sys.argv[2])
        e = bin(int(sys.argv[3]))
        e = e[2:len(e)]
        exponent = sys.argv[3]
        m = int(sys.argv[4])
else:
    b = int(sys.argv[1])
    e = bin(int(sys.argv[2]))
    e = e[2:len(e)]
    exponent = sys.argv[2]
    m = int(sys.argv[3])

if verbose:
    print("exponent(binary) = " + e)

    q = len(e) - 1
    r = 0
    while q > -1:
        if e[q] == '1':
            print(str(r),end = " ")
        q = q - 1
        r = r + 1
    print()


i = len(e) - 1
j = 0
eval = 1
steps = ""
while i > -1:
    bit = int(e[i])
    if bit == 0:
        j = j + 1
        i = i - 1
        continue
    x = ((b ** (bit * (2 ** j))) % m)
    eval = (eval * x) % m
    if verbose:
        print(str(b) + "^(" + str(bit) + "*2^" + str(j) + ') mod ' + str(m) + " = " + str(x) + " (mod " + str(m) + ")\n")
        steps += str(b) + "^(" + str(bit) + "*2^" + str(j) + ') mod ' + str(m) + " = " + str(x) + " (mod " + str(m) + ")\n"

    j = j + 1
    i = i - 1

if verbose:
    print(steps)

print(str(b) + "^" + exponent + " (mod " + str(m) + ") = " + str(eval))
