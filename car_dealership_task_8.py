class Car:
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def display_info(self):
        return f"Car: {self.make} {self.model}"


class Sedan(Car):
    def __init__(self, make, model, doors):
        super().__init__(make, model)
        self.doors = doors

    def display_info(self):
        super().display_info()
        return f"{super().display_info()}\nDoors: {self.doors}"


class SUV(Car):
    def __init__(self, make, model, seats):
        super().__init__(make, model)
        self.seats = seats

    def display_info(self):
        super().display_info()
        return f"{super().display_info()}\nSeats: {self.seats}"


class SportsCar(Car):
    def __init__(self, make, model, top_speed):
        super().__init__(make, model)
        self.top_speed = top_speed

    def display_info(self):
        super().display_info()
        return f"{super().display_info()}\nTop speed: {self.top_speed} km\h"


sedan = Sedan("Toyota", "Camry", 4)
suv = SUV("Ford", "Explorer", 7)
sports_car = SportsCar("Ferrari", "488 GTB", 330)

print(sedan.display_info())
print("-------------------------")
print(suv.display_info())
print("-------------------------")
print(sports_car.display_info())
