def is_leap_year(year):
    if 1600 <= year <= 4000:
        if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
            return True
        else:
            return False
        
# https://www.codewars.com/kata/526c7363236867513f0005ca/train/python