def lottery(s):
    answer = ""
    for i in s:
        if i.isdigit() and i not in answer:
            answer += i
    return answer or "One more run!"

# https://www.codewars.com/kata/5832db03d5bafb7d96000107/train/python