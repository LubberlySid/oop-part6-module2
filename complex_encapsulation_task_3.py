class Car:
    def __init__(self, make, model, year, mileage):
        self.__make = make
        self.__model = model
        self.year = year
        self.mileage = mileage

    def get_make(self):
        return self.__make

    def get_model(self):
        return self.__model

    def get_year(self):
        return self.year

    def get_mileage(self):
        return self.mileage

    def drive(self, new_mileage):
        self.mileage += new_mileage
        if self.mileage >= 300000:
            print("This car can't drive. Mileage is so high")
        return self.mileage


car = Car("BMW", "M5", 2019, 55000)
print(car. get_make())
print(car.get_model())
print(car.get_year())
print(car.get_mileage())
car.drive(20000)
print(car.get_mileage())
car.drive(300000)
