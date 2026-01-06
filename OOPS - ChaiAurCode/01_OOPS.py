# 1. Basic Class and Object
# Problem: Create a Car class with attributes like brand and model. Then create an instance of this class.

class Car:

    total_car = 0

    def __init__(self, brand, model):
        self.__brand = brand
        self.model = model
        Car.total_car +=1

    def get_brand(self):
        return self.__brand

    def full_name(self):
        return f"{self.__brand} {self.model}"
    
    def fuel_type(self):
        return "Petrol or Deisel"

class ElectricCar(Car):
    def __init__(self, brand, model, batterySize):
        super().__init__(brand, model)
        self.batterySize = batterySize

    def fuel_type(self):
        return "Electric Charge"


teslaCar = ElectricCar("Tesla", "Model Y", "85kWh")
# print(teslaCar.brand)
print(teslaCar.batterySize)
print(teslaCar.full_name())
print(teslaCar.get_brand())
print(teslaCar.fuel_type())


my_car = Car("Maruti", "Baleno")
# print(my_car.brand)
print(my_car.model)
print(my_car.full_name())

my_new_car = Car("Maruti", "Verna")
# print(my_car.brand)
print(my_car.model)
print(my_new_car.full_name())

print(my_new_car.fuel_type())

print(Car.total_car)