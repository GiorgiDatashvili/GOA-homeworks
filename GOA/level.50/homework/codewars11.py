def bmi(weight, height):
    if weight / height ** 2 <= 18.5:
        return "Underweight"
    elif weight / height ** 2 <= 25.0:
        return "Normal"
    elif weight / height ** 2 <= 30.0:
        return "Overweight"
    elif weight / height ** 2 > 30:
        return "Obese"
# https://www.codewars.com/kata/57a429e253ba3381850000fb/train/python