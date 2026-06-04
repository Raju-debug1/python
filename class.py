class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

my_car = Car("Jack's Monster Truck", "Vintage", 1990)
print(my_car.make)  
print(my_car.model)  
print(my_car.year)   
print(my_car) 

# Base Class (Parent) - Needed for electricCar to inherit from
class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

# Derived Class (Child)
class ElectricCar(Car):
    def __init__(self, make, model, year, battery_size):
        super().__init__(make, model, year)
        self.battery_size = battery_size  # Fixed indentation

    def battery_info(self):  # Moved out of __init__ and fixed indentation
        print(f"This car has a {self.battery_size}-kWh battery.")

# Execution Code (Moved outside the class definition)
e_car = ElectricCar("Tesla", "Model S", 2020, 100)
print(e_car.make)
e_car.battery_info()