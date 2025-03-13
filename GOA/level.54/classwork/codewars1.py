def number(bus_stops):
    sum=0
    for i in bus_stops:
        sum+=i[0]-i[1]
    return sum

# https://www.codewars.com/kata/5648b12ce68d9daa6b000099/train/python