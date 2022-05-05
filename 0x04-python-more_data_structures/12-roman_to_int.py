#!/usr/bin/python3
def roman_to_int(roman_string):
    if not roman_string or type(roman_string) != str:
        return(0)
    if not roman_string:
        return(0)
    out = 0
    num = {
        'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000
    }
    for i in range(len(roman_string)):
        if i > 0 and num[roman_string[i]] > num[roman_string[i - 1]]:
            out += num[roman_string[i]] - 2 * num[roman_string[i - 1]]
        else:
            out += num[roman_string[i]]
    return(out)
