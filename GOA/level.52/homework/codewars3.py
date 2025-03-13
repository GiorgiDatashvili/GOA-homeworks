def string_clean(s):
    numbers = "0123456789"
    for i in numbers:
        s = s.replace(i , "")
    return s

# https://www.codewars.com/kata/57e1e61ba396b3727c000251/train/python