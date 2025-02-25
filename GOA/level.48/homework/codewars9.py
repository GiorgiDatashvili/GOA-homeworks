def is_isogram(string):
    if len(string) <= 0:
        return True
    string = string.lower()
    for letter in string:
        if string.count(letter) > 1: 
            return False
    return True

# https://www.codewars.com/kata/54ba84be607a92aa900000f1/train/python