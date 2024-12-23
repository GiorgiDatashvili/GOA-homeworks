def highest_and_lowest(x):
    x = x.split()
    highest = max(x)
    lowest = min(x)
    return f"({highest} {lowest})"
print(highest_and_lowest("1 2 3 4 5"))
