name = input("რა გქვია?")
res = " "
for i in (name):
    res += i + " "
print(res)

numbers = input("აირჩიე საიდან-სადამდე გინდა რიცხვები რომ დაიწეროს")
for i in range(int(numbers)):
    if i % 2 and i % 3:
        print("ეს ციფრი არის 2ის და 3ის ჯერადი")
    else:
        print("ეს რიცხვი არ არის 2ის და 3ის ჯერადი")


num1 = input("აირჩიე რიცხვი")
num2 = input("აირჩიე მეორე რიცხვი")
num3 = input("აირჩიე მესამე რიცხვი")
num4 = input("აირჩიეთ მეოთხე რიცხვი")
num5 = input("აირჩიე მეხუთე რიცხვი")
print((int(num1) + int(num2) + int(num3) + int(num4) + int(num5)) // 5)

for i in range(-100 , 100):
    if i >= 0:
        print("ეს რიცხვი დადებითია")
    else:
        print("ეს რიცხვი უარყოფითია")


for i in range(1,10):
    print("*" * i + " " *(18-2 * i) + "*" * i)


