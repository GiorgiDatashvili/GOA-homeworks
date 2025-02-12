def odd_or_even(arr):
    if sum(arr) % 2 == 0:
        return "even"
    elif sum(arr) % 2 != 0:
        return "odd"
    elif len(arr) == 0:
        return "even"
# https://www.codewars.com/kata/5949481f86420f59480000e7/train/python