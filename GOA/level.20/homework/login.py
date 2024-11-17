username = input("Type your username:")
name = input("Type your name:")
last_name = input("Type your last name:")
age = input("Type your age:")
if int(age) < 13:
    print("You are underaged and not allowed to visit the site")
elif int(age) >= 13:
    print("You are allowed to visit the site")
    password = input("Type your password:")
    if password != "giorgi123":
        print("Wrong password")
    else:
        print("Log in succesful")
        

