# Jason Martin
    # CS608-001 Crpytography
        # Midterm Exam Program
            # October 27, 2021

import sys

if len(sys.argv) < 3:
    print("<program usage: python* encode.py <-e/-d> <text to encode/decode>\n")
    sys.exit()

if sys.argv[1] == "-e":
    plaintext = sys.argv[2].lower()
    encode = ''

    for char in plaintext:
        digits = ""
        if ord(char) - 97 < 10:
            digits = '0' + str(ord(char)-97)
        else:
            digits = str(ord(char)-97)
        encode += digits

    print("Numerical value of message " + sys.argv[2] + " is " + encode)

elif sys.argv[1] == "-d":
    encoded = sys.argv[2]
    decoded = ""
    i = 0
    while i < len(encoded):
        decoded += str(chr(int(encoded[i:i+2])+97))
        i = i + 2

    print("Alphabetical value of message " + encoded + " is " + decoded)

else:
    print("<program usage: python* encode.py <-e/-d> <text to encode/decode>\n")
    sys.exit()
