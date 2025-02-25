def human_years_cat_years_dog_years(human_years):
    cat_year = (human_years-2)*4
    dog_year = (human_years-2)*5
    if human_years == 1:
        return [1,15,15]
    elif human_years >= 2:
        return [human_years,24+cat_year,24+dog_year]

# https://www.codewars.com/kata/5a6663e9fd56cb5ab800008b/train/python