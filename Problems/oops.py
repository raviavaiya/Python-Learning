#create a class called Car and attribute like Brand and Model

class Car:
    total_car = 0
    def __init__(self, brand, model):
        # private attribute brand
        self.__brand = brand
        self.__model = model
        Car.total_car += 1

    # static method to get the General information
    @staticmethod
    def genral_info():
        return "Cars are used for transportation."

    @property
    def model(self):
        return self.__model


    def fuel_type(self):
        return "Petrol or Diesel"
    
    def get_brand(self):
        return self.__brand + "!!!"

    # Method to return the full name of the car
    def fullname(self):
        return f"{self.__brand} and {self.__model}"

# car = Car("Toyota", "Corolla")
# car.model = "Camry"
# print(car.model)
# print(car.model)

# print(car.genral_info(),car.get_brand(),car.fuel_type())
# print(Car.genral_info())
# Create an object of the Car class

# Inherit from the Car class to create a new class called ElectricCar
class ElecticCar(Car):
    def __init__(self, brand, model, battery_size):
        # Call the constructor of the parent class
        super().__init__(brand, model)
        # Initialize the battery size attribute
        self.battery_size = battery_size

    def fuel_type(self):
        return "Electric"



class Battery:
    def battery_info(self):
        return "This is Battery"
    

class Engine:
    def engine_info(self):
        return "This is Engine"


class Electic(Battery,Engine, Car):
    pass



tesla = Electic("Tesla", "Model S")
print(tesla.battery_info()) # This is Battery
print(tesla.engine_info()) # This is Engine
print(tesla.fullname()) # Tesla and Model S
# print(tesla.fuel_type()) # Electric
# car1= Car("Toyota", "Corolla")
# # Accessing the attributes of the ElectricCar object
# my_tesla = ElecticCar("Tesla", "Model S", "100 kWh")
# print(isinstance(my_tesla, Car)) # True
# print(isinstance(my_tesla, ElecticCar)) # True
# print(isinstance(car1, Car))
# print(isinstance(car1, ElecticCar))
