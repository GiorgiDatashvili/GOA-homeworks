def to_alternating_case(string):
    strn = ""
    for i in string:
        if i.isupper():
            strn += i.lower()
        else:
            strn += i.upper()
    return strn

# https://www.codewars.com/kata/56efc695740d30f963000557/train/python