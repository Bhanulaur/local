# Define a class
class Car:
    # Constructor (initializer method)
    def __init__(self, brand, model, year):
        # Attributes of the class
        self.brand = brand
        self.model = model
        self.year = year

    # Method to display car information
    def display_info(self):
        print(f"Car: {self.brand} {self.model}, Year: {self.year}")

    # Method to simulate driving
    def drive(self):
        print(f"The {self.model} is now driving.")

# Create objects of the Car class (instances)
car1 = Car("Tesla", "Model S", 2022)
car2 = Car("Ford", "Mustang", 1969)

# Access methods and attributes
car1.display_info()  # Output: Car: Tesla Model S, Year: 2022
car2.display_info()  # Output: Car: Ford Mustang, Year: 1969

car1.drive()  # Output: The Model S is now driving.
car2.drive()  # Output: The Mustang is now driving. 
cae  bjknon iumb
