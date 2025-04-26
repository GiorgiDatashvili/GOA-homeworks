class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year
    def car_info(self):
        return f"{self.brand}, {self.model}, {self.year}"
c1 = Car("BMW", "M8 Competition Gran Coupe", 2019)
print(c1.car_info())