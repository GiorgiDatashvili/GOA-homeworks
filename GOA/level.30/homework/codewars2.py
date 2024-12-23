def square_sum(numbers):
    sqr_numbers = [ ]
    for i in numbers:
        sqr_numbers.append(i ** 2)
    return sum(sqr_numbers)
print(square_sum([1,5,5]))
#https://www.codewars.com/kata/515e271a311df0350d00000f