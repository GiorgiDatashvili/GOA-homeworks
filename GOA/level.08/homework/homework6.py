age = input("რამდენი წლის ხარ")
print(13 < int(age) < 19)

mark = input("რა ქულა მიიღე საკონტროლოზე?")
is_A = int(mark) >= 9
is_B = 9 > int(mark) >= 8
is_C = 8 > int(mark) >= 7
is_D = 7 > int(mark) >= 6
is_F = 6 > int(mark) 
print(is_A)
print(is_B)
print(is_C)
print(is_D)
print(is_F)



a = 5 > 4 # True
b = 10 > 12 # False
print(a and b)
print(b and a)
print(a or b)
print(b or a)


num1 = 50
num2 = 40
print(num1 > num2)
print(num1 < num2)
print(num1 == num2)
print(num1 <= num2)
print(num1 >= num2)
print(num1 != num2)


c = 20
x = 40
y = 50

is_c_greatest = c > x > y #False
is_x_middle = y > x > c # True
is_y_least = x > c > y # False

score = 100
is_pass = score >= 50 # True
is_high_pass = score >= 75 , score >= 90 #False
is_perfect = score == 100 #True
is_failing = score < 50 #False

P = True
Q = False
P_and_not_Q = True
not_P_and_Q = False
P_xor_Q = True
