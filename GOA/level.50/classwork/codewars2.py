def accum(st):
    answer = ""
    count = 0
    for i in st:
        answer += i.upper() + i.lower() * count + "-"
        count += 1
    return answer[:-1]

# https://www.codewars.com/kata/5667e8f4e3f572a8f2000039/train/python