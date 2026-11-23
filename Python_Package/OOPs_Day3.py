# Polymorphism: Greek words (Poly=>Many, Morph=>Forms)=>Many forms
# It refers to the ability to use a single interface (method, class) to represent directly underlying forms

# Can be implemented in different ways:
# 1. Method Overloading: having multiple methods with the same name (Directly not supported in python)
'''
class Maths:

    def add_numbers(self,a,b,c=0,d=0):
        return(a+b+c+d)

obj = Maths()
sum1 = obj.add_numbers(10,20,30,40)
print(sum1)

sub2 = obj.add_numbers(10,20)
print(sub2)

# 2. Method Overriding (using the same method in parent and child class)
class Vehicle:
    def start(self):
        print("Vehicle starts...")

    def stops(self):
        print("Vehicle stops...")

class Car(Vehicle):
    def start(self):
        print("Car starts...")

    def honk(self):
        print ("Car Beeps...")
c = Car()
c.start()
c.stops()
c.honk()

v = Vehicle()
v.start()
v.stops()

# Operator overloading

class OperatorOverLoading:
    def __init__(self,num1,num2,str1,str2):
        self.sum_num = num1 + num2
        self.concatenate_strings=str1+str2

    def printMethod(self):
        print(self.sum_num)
        print(self.concatenate_strings)

o1 = OperatorOverLoading(10,20,"ETL"," QA Labs")
o2 = OperatorOverLoading(10,20,"10","20")
#o.printMethod()
o1.printMethod()
o2.printMethod()

# 4. Class Polymorphism in Python

class Cirlce:
    def area(self):
        return 3.14*5*5

class Square:
    def area(self):
        return 5*5

class Triangle:
    def area(self):
        return 0.5*5*4

c=Cirlce()
s=Square()
t=Triangle()
shapes=[c,s,t]

for obj in shapes:
    print(obj.area())


from pandas.errors import AbstractMethodError


# Abstraction: Hiding Complexity of the system from end user
# Abstract Class: We can't create an object of abstract
# Abstract Method: Missing implementation

# Concrete Class
class Vehicle:
    def start(self):
        print("Starts Vehicle")

    def stops(self):
        print("Stops Vehicle")
v = Vehicle()
v.start()
v.stops()
'''
# Abstract Class
from abc import ABC, abstractmethod
class Vehicle(ABC):
    @abstractmethod
    def start(self):
        pass
        #print("Starts Vehicle")
    @abstractmethod
    def stop(self):
        #print("Stops Vehicle")
        pass
    def honk(self):
        print("Car Honks...")

class car(Vehicle):
    def start(self):
        print("Car Starts...")
    def stop(self):
        print("Car Stops...")

class Bike(Vehicle):
    def start(self):
        print("Bike Starts...")
    def stop(self):
        print("Bike Stops...")

c = car()
c.start()
c.stop()
c.honk()

b=Bike()
b.start()
b.stop()
b.honk()