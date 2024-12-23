def count_positives_sum_negatives(arr):
    if not arr:  
        return []
    count_positive = 0
    sum_negative = 0
    i = 0
    for i in arr:
        if i > 0:
            count_positive += 1
        elif i < 0:
            sum_negative += i
    return f"[{count_positive} {sum_negative}]"
print(count_positives_sum_negatives([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -11, -12, -13, -14, -15]))

#https://www.codewars.com/kata/576bb71bbbcf0951d5000044