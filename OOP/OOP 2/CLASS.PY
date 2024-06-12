# class Students :
#     name = "keran"

# s1 = Students()
# print(s1.name)

# s2 = Students()
# print(s2.name)


class Car:
    # defaut constructors (we dont use multiple default constructors)
    def __init_subclass__(self):
        pass

    # parameterized constructer
    def __init__(self, fullname, marks):
        # fullname is an parameter in this function and self is referance of that class it can be named anything (self is recommended widely used in industry level)
        self.fulname = fullname
        self.marks = marks
        print("creating new  class in python ")


car1 = Car("dhiren", 98)
print(car1.fulname, car1.marks)
# while printing   only the parameter matching constructer will print

#     color= "blue"
#     brand = "benz"
#     level = 'G'

# car1 = Car()
# print(car1.color)
# print(car1.level)
