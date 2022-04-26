#!/usr/bin/python3
for letters in range(ord('a'), ord('z')+1):
    letter_q = chr(letters)
    if letter_q not in "qe":
        print(letter_q, end='')
