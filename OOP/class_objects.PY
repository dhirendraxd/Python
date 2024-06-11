class Car:  #here, Car is an class 

    def __init__(self, mybrand, mymodell):
        self.brand = mybrand
        self.modell = mymodell

my_car = Car("toyota", "corolla")
#my_car is an object in this code block 
print(my_car.brand) #Output :toyota
print(my_car.modell) #Output :corolla

my_new_car = Car("tata", "safari")
print(my_new_car.modell) #Ouput :safari