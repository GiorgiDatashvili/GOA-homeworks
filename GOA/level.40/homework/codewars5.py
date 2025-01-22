def factorial(n):
    answer = n
    if n == 0:
        return 1
    for i in range(1 , n):
        answer *= i
    return answer
#https://www.codewars.com/kata/57a049e253ba33ac5e000212/train/python