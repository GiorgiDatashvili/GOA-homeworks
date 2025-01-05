numbers = (2, 56, 99, 22, 15, 23, 66, 11, 134, 23, 66, 91, 22, 2, 23)
print(numbers[0],numbers[1])
print(numbers.count(23))

print("---------------------")
aura = (10, 25, 5, 80, 70, 20)
for i in aura:
    if i > 10:
        print(i)
    
# ლისტში მოდიფიკაცია შესაძლებელია, tuple-ში არა.
# immutable - არ შეგიძლია მოდიფიკაცია/შეცვლა mutable - შეგიძლია მოდიფიკაცია/შეცვლა 