class Car:  

    def __init__(self, mybrand, mymodell):
        self.brand = mybrand
        self.modell = mymodell
    
    def full_name(self):
        return f"{self.brand}{self.modell}"





my_car = Car("toyota", "corolla")
print(my_car.brand) 
print(my_car.modell) 
print(my_car.full_name())

my_new_car = Car("tata", "safari")
print(my_new_car.modell) 