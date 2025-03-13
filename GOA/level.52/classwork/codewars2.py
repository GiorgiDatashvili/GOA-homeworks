def min_max(lst):
    minimum = 0
    maximum = 0
    min_and_max = []
    for i in lst:
        minimum = min(lst)
        maximum = max(lst)
    min_and_max.append(minimum)
    min_and_max.append(maximum)
    return min_and_max
# https://www.codewars.com/kata/559590633066759614000063/train/python