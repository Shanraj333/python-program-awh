class Car:
    def car_details(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def display_details(self):
        print(f"{self.brand} {self.model} {self.year}")


car1 = Car()
car2 = Car()

car1.car_details("Toyota", "Corolla", 2020)
car2.car_details("Tesla", "Model 3", 2023)


print("Car 1:", end=" ")
car1.display_details()

print("Car 2:", end=" ")
car2.display_details()

