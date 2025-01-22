def digitize(n):
    digits = []
    for digit in str(n): 
        digits.append(int(digit))
    return digits[::-1]

# https://www.codewars.com/kata/5583090cbe83f4fd8c000051/train/python