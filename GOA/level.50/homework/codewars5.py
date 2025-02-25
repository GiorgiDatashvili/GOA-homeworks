def longest(a1, a2):
    new = sorted(a1 + a2)
    list = ""
    for i in new:
        if i not in list:
            list = list + i
    return list
# https://www.codewars.com/kata/5656b6906de340bd1b0000ac/train/python