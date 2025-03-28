def elimination(arr):
    for i in arr:
        if arr.count(i) > 1:
            return i
        else:
            continue
    return None

# https://www.codewars.com/kata/5834315e06f227a6ac000099/train/python