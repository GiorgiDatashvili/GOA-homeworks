def find_next_square(sq):
    if int(sq ** 0.5) == sq ** 0.5:
        return ((sq ** 0.5)+1) ** 2
    else:
        return -1

# https://www.codewars.com/kata/56269eb78ad2e4ced1000013/train/python