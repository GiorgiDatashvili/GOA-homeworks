def solve(s):
    count_upper = 0
    count_lower = 0
    for i in s:
        if i.isupper():
            count_upper += 1
        elif i.islower():
            count_lower += 1
    if count_upper > count_lower:
        return s.upper()
    elif count_lower > count_upper:
        return s.lower()
    elif count_lower == count_upper:
        return s.lower()
# https://www.codewars.com/kata/5b180e9fedaa564a7000009a/train/python