def high_and_low(numbers):
    new_numbers = list(int(i) for i in numbers.split())
    maximum = max(new_numbers)
    minimum = min(new_numbers)
    return f"{maximum} {minimum}"
        
# https://www.codewars.com/kata/554b4ac871d6813a03000035/train/python