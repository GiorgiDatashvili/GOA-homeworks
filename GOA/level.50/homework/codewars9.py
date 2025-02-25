def printer_error(s):
    count = []
    for i in s:
        if i < "a" or i > "m":
            count.append(i)
    answer = f"{len(count)}/{len(s)}"
    return answer
# https://www.codewars.com/kata/56541980fa08ab47a0000040/train/python