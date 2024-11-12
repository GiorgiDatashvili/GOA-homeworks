number = input("აირჩიე რიცხვი 1-100მდე:")
if int(number) > 10:
    print("შენი რიცხვი 10ზე მეტია")
elif int(number) == 10:
    print("შენი რიცხვია 10")
else:
    print("შენი რიცხვი 10ზე ნაკლებია")



num1 = input("აირჩიე ნებისმიერი რიცხვი:")
if int(num1) %2 == 0:
    print("შენი რიცხვი ლუწია")
else:
    print("შენი რიცხვი კენტია")



num2 = input("შემოიტანე რიცხვი:")
if int(num2) > 0:
    print("შენი რიცხვი დადებითია")
elif int(num2) == 0:
    print("შენი რიცხვი არც უარყოფითია და არც დადებითი")
else:
    print("შენი რიცხვი უარყოფითია")



num3 = input("შემოიტანე პირველი რიცხვი:")
num4 = input("შემოიტანე მეორე რიცხვი:")
if num3 == num4:
    print("შენი რიცხვები ტოლია")
else:
    print("შენი რიცხვები არ არის ტოლი")



num5 = input("შემოიტანე რიცხვი 1-1000 შორის:")
if int(num5) > 100 and int(num5) %2 :
    print("შენი რიცხვი 100ზე მეტია და ლუწია")
elif int(num5) == 100:
    print("შენი რიცხვია 100")
else:
    print("შენი რიცხვი არ არის 100ზე მეტი")



num6 = input("აირჩიე რიცხვი 1-50ს შორის:")
if int(num6) % 5 == 0 or int(num6) % 10 == 0 :
    print("შენი რიცხვი 5ის ან 10ის ჯერადია") 
else:
    print("შენი რიცხვი არ არის 5ის ან 10ის ჯერადი")


rows = 5
for i in range(rows):
    print(" " * (rows - i - 1), end="")
    print("*" * (2 * i + 1))
    

item1 = input("შემოიტანე ნებისმიერი ნივთი")
item2 = input("შემოიტანე მეორე ნივთი")
item3 = input("შემოიტანე მესამე ნივთი")
item4 = input("შემოიტანე მეოთხე ნივთი")
item5 = input("შემოიტანე მეხუთე ნივთი")

arr =[ item1 , item2 , item3 , item4 , item5]
print(arr[0])
print(arr[1])
print(arr[2])
print(arr[3])
print(arr[4])

arr = [9,5,94,711,52,96,71,8]
min_number = arr[0]
for number in arr:
    if min_number > number:
        min_number = number
print(min_number)

names = ["giorgi" , "nikolozi", "saba", "luka"]
print(names[0])
print(names[1])
print(names[2])
print(names[3])

name = ["davit", "gio", "davit", "gio", "davit"]
count_davit = 0
for n in name:
    if n == "davit":
        count_davit += 1
print("დავითი" ,count_davit, "ჯერ გამოჩნდა სიაში")


hi = "hello"
print(hi[::-1])

list = [5, 10, 15, 20]
sashualo = (list[0]+list[1]+list[2]+list[3])//4
print(sashualo)
   
   

