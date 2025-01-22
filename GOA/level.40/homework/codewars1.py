def remove_duplicate_words(s):
    new_list = []
    new_arr = s.split()
    for i in new_arr:
        if i not in new_list:
            new_list.append(i)
    return " ".join(new_list)

# https://www.codewars.com/kata/5b39e3772ae7545f650000fc/train/python