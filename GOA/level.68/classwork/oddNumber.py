find_odd = lambda a,b:a if a % 2 != 0 else b if b % 2 != 0  else "Odd Number Not Found"
print(find_odd(1,4))