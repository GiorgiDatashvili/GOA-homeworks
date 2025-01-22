def capitals(word):
    answers = []
    index = 0
    for i in word:
        if i.isupper():
            answers.append(index)
        index +=1
    return answers
# https://www.codewars.com/kata/539ee3b6757843632d00026b/train/python