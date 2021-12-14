# Jason Martin
    # CS608-001 Crpytography
        # Midterm Exam Program
            # October 27, 2021

a = 2
b = 179
c = 3631




p = 1299898

g = 2

while g < p - 1:
    b = g

    e = bin(p//a)
    e = e[2:len(e)]
    m = p
    i = len(e) - 1
    j = 0
    eval = 1
    while i > -1:
        bit = int(e[i])
        if bit == 0:
            j = j + 1
            i = i - 1
            continue
        x = ((b ** (bit * (2 ** j))) % (m+1))
        eval = (eval * x) % (m+1)

        j = j + 1
        i = i - 1

    if eval == 1:
        g = g + 1
        continue





    e = bin(p//b)
    e = e[2:len(e)]
    m = p
    i = len(e) - 1
    j = 0
    eval = 1
    while i > -1:
        bit = int(e[i])
        if bit == 0:
            j = j + 1
            i = i - 1
            continue
        x = ((b ** (bit * (2 ** j))) % (m+1))
        eval = (eval * x) % (m+1)

        j = j + 1
        i = i - 1


    if eval == 1:
        g = g + 1
        continue





    e = bin(p//c)
    e = e[2:len(e)]
    m = p
    i = len(e) - 1
    j = 0
    eval = 1
    while i > -1:
        bit = int(e[i])
        if bit == 0:
            j = j + 1
            i = i - 1
            continue
        x = ((b ** (bit * (2 ** j))) % (m+1))
        eval = (eval * x) % (m+1)

        j = j + 1
        i = i - 1


    if eval == 1:
        g = g + 1
        continue


    g = g + 1
    print(g)
