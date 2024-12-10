text = input("Write a word: ")
name = input("Write your name: ")
def search():
    sentence = input("Write a sentence: ")
    new_sentence = sentence.split()
    for i in new_sentence:
        if i == text or i == name:
            print("Word found")
search()