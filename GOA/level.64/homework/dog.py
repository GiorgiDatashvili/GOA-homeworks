class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def bark(self):
        return "Woof!"
d1 = Dog("Max", 2)
print(d1.bark())
        