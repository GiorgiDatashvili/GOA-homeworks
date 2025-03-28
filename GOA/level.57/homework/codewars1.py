def vowel_one(s):
    answer = ""
    vowels = "aeiouAEIOU"
    for i in s:
        if i in vowels:
            answer += "1"
        else:
            answer += "0"
    return answer

# https://www.codewars.com/kata/580751a40b5a777a200000a1/train/python