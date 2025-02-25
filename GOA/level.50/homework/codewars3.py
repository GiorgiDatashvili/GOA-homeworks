def is_triangle(a, b, c):
    if a >= b+c or b >= a+c or c >= a+b:
        return False
    return True
# https://www.codewars.com/kata/56606694ec01347ce800001b/train/python