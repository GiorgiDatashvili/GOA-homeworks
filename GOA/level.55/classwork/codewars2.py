def no_boring_zeros(n):
    if len(str(n)) == 1:
        return 0
    else:  
        n = str(n).rstrip("0")
        return int(n)

# https://www.codewars.com/kata/570a6a46455d08ff8d001002/train/python