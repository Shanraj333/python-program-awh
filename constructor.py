class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def display_details(self):
        print(f"{self.brand} {self.model} {self.year}")


car1 = Car("Toyota", "Corolla", 2020)
car2 = Car("Tesla", "Model 3", 2023)
print("Car 1:", end=" ")
car1.display_details()

print("Car 2:", end=" ")
car2.display_details()