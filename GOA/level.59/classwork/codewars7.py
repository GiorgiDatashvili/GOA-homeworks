def array_diff(a, b):
    answer = []
    for i in a:
        if i not in b:
            answer.append(i)
    return answer

# https://www.codewars.com/kata/523f5d21c841566fde000009/train/python