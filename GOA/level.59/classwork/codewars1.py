def calculator(x, y, op):
     if type(x) not in [int, float] or type(y) not in [int, float]:
        return "unknown value"
     if op == "+":
        return x + y
     elif op == "-":
        return x - y
     elif op == "*":
        return x * y
     elif op == "/" and y != 0:
        return x / y
     else:
        return "unknown value"
     
# https://www.codewars.com/kata/5810085c533d69f4980001cf/train/python