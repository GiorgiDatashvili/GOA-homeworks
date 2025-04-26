class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def lower(self):
        return self.name.lower()
    def __str__(self):
        return f"{self.name} {self.age}"
    
p1 = Person("Giorgi", 17)
print(p1.lower())
print("---------------")
class Human:
     def __init__(self, name, age):
        self.name = name
        self.age = age
     def __str__(self):
        return f"{self.name} {self.age}"
p2 = Human("Giorgi", 17)
print(p2)
