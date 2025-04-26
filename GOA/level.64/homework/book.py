class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year
    def info(self):
        return f"{self.title}, {self.author}, {self.year}"
b1 = Book("Crime and Punishment", "Fyodor Dostoevsky", 1866)
print(b1.info())