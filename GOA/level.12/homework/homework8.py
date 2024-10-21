#1
for i in range(1 , 50 , 2):
    print("GOA")

print("----------")
print("----------")

# 2
# for 

for i in range(5):
    print("*" * 5)

# while
print("----------")
print("----------")

i = 0
while i < 5:
    print("*" * 5)
    i += 1

print("----------")
print("----------")
# 3
# for

for i in range(5):
    print("*" * 4)

print("----------")
print("----------")

# while
i = 0
while i < 5:
    print("*" * 4)
    i += 1


# 4
num1 = 5
num = 7
for i in range(num):
    print(num1 * num)
    

print("----------")
print("----------")

# 5

user_password =input("Enter your password: ")
password = "12345"
while user_password != password:
    user_password=input("Try Again: ")
print("Log in Succesful")