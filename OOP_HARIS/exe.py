from random import randint
class programmmers:
    company = "microsoft"
    def __init__(self, name , salary ,pincode) :
        self.name = name
        self.pin = pincode
        self.salary = salary
        
        
p = programmmers("dhiren", 232, 432234)
print(p.company,p.pin,p.salary)
r = programmmers("hitesh", 43, 52343)
print(r.company, r.pin, r.salary)



#Q2
class calculator:
    def __init__(self,n):
        self.n = n
        
    def square (self):
        print(f"the square is{self.n*self.n}")
        
    def cube (self):
        print(f"the square is{self.n*self.n*self.n}")
        
    @staticmethod
    def hello():
        print("hello")

    def squareroot (self):
        print(f"the square is{self.n**1/2}")

a =calculator(4)
a.square()
a.hello()



#q3
class demo:
    a = 4
o=demo()
print(o.a)
o.a=1
print(o.a)
#this doesnot change the values inside the class only for this particular scenario it changes its values 
print(demo.a)# this shows that it didnt chnaged the vlaues inside the classs



#   Q4  
#Q5
class Train:
    def book(self, trainnum, fro, to):
        print(f"Ticket is booked in train no {trainnum} from {fro} to {to}")
    
    def getstatus(self, trainnum):
        print(f"Train {trainnum} is running")
    
    def getfare(self, trainnum, fro, to):
        print(f"Fare details for train {trainnum} from {fro} to {to}")

# Creating an instance of Train
t = Train()

# Booking a ticket
t.book(43, "Raipur", "Delhi")

# Getting status of the train
t.getstatus(43)

# Getting fare of the train
t.getfare(43, "Raipur", "Delhi")
