def even_or_odd(s):
    sum_of_odds = 0
    sum_of_even = 0
    for i in str(s):
        if int(i) % 2 == 0:
            sum_of_even += int(i)
        elif int(i) % 2 != 0:
            sum_of_odds += int(i)
    if sum_of_even > sum_of_odds:
        return "Even is greater than Odd"
    elif sum_of_odds > sum_of_even:
        return "Odd is greater than Even"
    elif sum_of_even == sum_of_odds:
        return "Even and Odd are the same"
            
# https://www.codewars.com/kata/57f7b8271e3d9283300000b4/train/python