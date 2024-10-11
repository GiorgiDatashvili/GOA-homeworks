# 1
age = input("რამდენი წლის ხარ? ")
for i in range(10):
    print("შენ ხარ " + age + " წლის.")

# 2
celsius = input("რამდენი გრადუსია გარეთ?")

celsius = float(celsius)

fahrenheit = (celsius * 9/5) + 32

print(fahrenheit)


#3

num1 = 5 > 3
num2 = 3 > 5
num3 = 7 > 10
num4 = 10 > 7
num5 = 55 > 54
num6 = 54 > 55

print(num1 or num2)
print(num1 and num2)

print(num3 and num4)
print(num3 or num4)

print(num5 or num6)
print(num5 and num6)

# 4
for i in range(5):
    print("*" * i)


# 5
age = 20
print(18 < age)