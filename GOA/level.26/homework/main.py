from turtle import *
def naxazi():
    forward(100)
    left(120)
    forward(100)
    left(120)
    forward(100)
    left(120)
naxazi()
def samkutxedebi(x):
    for i in range(x):
        if i % 2 == 0 :
            pencolor("#3333ff")
        else:
            pencolor("#269900")
        naxazi()
speed(10)
samkutxedebi(120)
exitonclick()

def hello_world():
    print("print()")
hello_world()

def even_or_odd(x):
    for i in range(x):
        if i % 2 == 0:
            print("არ არის კენტი" , i ,"რიცხვი")
        else:
            print("კენტია" , i , "რიცხვი")
even_or_odd(25)

def otxkutxedi(g):   
        for i in range(g):
            print("*" * 6)
            print("*" * 6)
            print("*" * 6)
            print("*" * 6)
            print("----------", "Number", i)
otxkutxedi(120)
def umbrella():
    rows = 4
    for _ in range(120):
        for i in range(1, rows + 1):
            spaces = rows - i
            stars = 2 * i - 1
            print(" " * spaces + "*" * stars)
        for _ in range(2):
            print(" " * (rows - 1) + "*")
        print("-----------" , )
umbrella()

def rombi(h):
    row = 4
    for g in range(120):   
        for i in range(row):
            print(" " * i, end="")
            print("*" * 6)
rombi(120)