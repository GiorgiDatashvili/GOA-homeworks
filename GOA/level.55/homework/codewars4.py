def vowel_indices(words):
    word = words.lower()
    vowels = []
    i = 0
    for letter in word:
        i += 1
        if letter == "a" or letter == "e" or letter == "i" or letter == "o" or letter == "u" or letter == "y":
            vowels.append(i)
    return vowels

# https://www.codewars.com/kata/5680781b6b7c2be860000036/train/python