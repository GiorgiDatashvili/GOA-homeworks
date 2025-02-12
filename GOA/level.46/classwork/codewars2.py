def disemvowel(string_):
    result = ""
    for j in string_:
        if j not in "aeiouAEIOU":
            result += j
    return result

# https://www.codewars.com/kata/52fba66badcd10859f00097e/train/python