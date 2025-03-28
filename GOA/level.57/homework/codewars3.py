def count_letters_and_digits(s):
    n = 0
    for x in s:
        if x.isalpha() or x.isdigit():
            n += 1
    return n

# https://www.codewars.com/kata/5738f5ea9545204cec000155/solutions