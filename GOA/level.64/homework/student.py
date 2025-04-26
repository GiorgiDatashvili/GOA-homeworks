class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade
    def is_passing(self):
        if self.grade > 5:
            return True
        else:
            return False
s1 = Student("Giorgi",17,11)
print(s1.is_passing())