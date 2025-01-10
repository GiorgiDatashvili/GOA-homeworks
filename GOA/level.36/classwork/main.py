def digitize(n):
    digits = []
    for digit in str(n): 
        digits.append(int(digit))
    return digits[::-1]
print(digitize(1325))