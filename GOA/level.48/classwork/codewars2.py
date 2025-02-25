def find_short(s):
    lenghts = []
    words = s.split()
    for word in words:
        lenghts.append(len(word))
    return min(lenghts)
# https://www.codewars.com/kata/57cebe1dc6fdc20c57000ac9/train/python