def sort_by_length(arr):
    ans = []
    length = []
    for i in arr:
        length.append([len(i), i])
    for i in sorted(length):
        ans.append(i[1])
    return ans
# https://www.codewars.com/kata/57ea5b0b75ae11d1e800006c/train/python