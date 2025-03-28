def longest_word(string_of_words):
    answer = ""
    list_of_words = string_of_words.split()
    for i in list_of_words:
        if len(answer) <= len(i):
            answer = ""
            answer = i
    return answer

# https://www.codewars.com/kata/5939ab6eed348a945f0007b2/train/python