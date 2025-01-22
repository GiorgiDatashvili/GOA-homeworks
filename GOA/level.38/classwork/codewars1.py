def password(st):
    if len(st) < 8:
        return 0
    upper = 0
    lower = 0
    digit = 0
    for i in st:
        if i.isupper():
            upper = 1
        if i.islower():
            lower = 1
        if i.isdigit():
            digit = 1
    return (upper + lower + digit) == 3
            
# https://www.codewars.com/kata/56a921fa8c5167d8e7000053/train/python