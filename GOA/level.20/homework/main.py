letters = ["a","b","c","d","e"]
for i in range(len(letters)):
    if letters[i] == "a" or letters[i] == "e":
        letters[i] = "ხმოვანი"
print(letters)



numbers = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
for i in range(len(numbers)):
    if numbers[i] % 5 == 0 or numbers[i] % 3 == 0:
        print(numbers[i])


rows = 4
for i in range(rows):
    print(" " * i, end="")
    print("*" * 6)


age = int(input("რამდენი წლის ხარ?:"))
if age > 12:
    print("შენ არ ხარ 12 წლის")
elif age == 12:
    print("შენ ხარ 12 წლის")
    



        