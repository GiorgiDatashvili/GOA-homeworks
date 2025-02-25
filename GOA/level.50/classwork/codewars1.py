def is_isogram(string):
    return False if [i for i in string.lower() if string.lower().count(i) > 1] else True

# https://www.codewars.com/kata/54ba84be607a92aa900000f1/train/python