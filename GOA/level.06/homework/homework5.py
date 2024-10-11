#1
birthyear = input("როდის დაიბადე?")
currentyear = 2024
age = currentyear - int(birthyear)
print(age)

a = input("ოთხკუთხედის სიგრძეა")
b = input("ოთხკუთხედის სიგანეა")
ფართობი = int(a) * int(b)
პერიმეტრი = 2 * (int(a) + int(b))
print(ფართობი)
print(პერიმეტრი)

მანძილი = input("რა მანძილია შენი სახლიდან სკოლამდე?")

მანძილი_მეტრებში = int(მანძილი) * 1000
მანძილი_სანტიმეტრებში = int(მანძილი) * 100000
მანძილი_მილიმეტრებში = int(მანძილი) * 1000000
print(მანძილი_მეტრებში)
print(მანძილი_სანტიმეტრებში)
print(მანძილი_მილიმეტრებში)

name = input("რა გქვია?")
last_name = input("რა გვარის ხარ?")
parent_name = input("რა ჰქვია შენს მშობელს?")
parent_last_name = input("რა გვარია შენი მშობელი?")
favorite_color = input("რა არის შენი საყვარელი ფერი?")
favorite_car = input("რა არის შენი საყვარელი მანქანა")
favorite_hobby = input("რა არის შენი საყვარელი ჰობი")

print("ჩემი სახელი და გვარია",name,last_name,",ჩემი მშობლის სახელი და გვარია",parent_name,parent_last_name,",ჩემი საყვარელი ფერია",favorite_color,",ჩემი საყვარელი მანქანაა",favorite_car,"და ჩემი საყვარელი ჰობია",favorite_hobby)

number = input("აირჩიე რამე ორნიშნა რიცხვი")
number1 = input("აირჩიე ამ ორნიშნა რიცხვიდან ციფრი")
number2 = int(number) // int(number1)
number3 = int(number1) + int(number2)
print(number3)
