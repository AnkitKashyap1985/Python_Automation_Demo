# Inheritance
'''
class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        print("inside constructor - Brand name is:", self.brand)
        self.model_name = model
        print("Model Name is:", self.model_name)

    def start_engine(self):
        print("Vehicle starts...burrrrr....")

    def stop_engine(self):
        print("Vehicle stops...")

class Car(Vehicle):
    def __init__(self, brand, model, fuel_type):
        super().__int__(brand, model)
        self.fuel_type = fuel_type

    def honk(self):
        print(f"{self.brand} {self.model_name} is honking: beep beep")

class Car(Vehicle):
    def __init__(self, brand, model, fuel_type):
        c = Car("Maruti Suzuki", "Breeza", "Petrol")
        print(c.fuel_type)
        print(c.brand)
        print(c.model_name)
        c.start_engine()
        c.stop_engine()
        c.honk()

v1 = Vehicle("Tesla","ModelS")



v1 = Vehicle("Mahindra","XUV700")
print("Outside Constructor - ",v1.brand)
print("Outside Constructor - ",v1.model_name)

v1 = Vehicle("Hyndai","Nios Sportz")
print("Outside Constructor - ",v1.brand)
print("Outside Constructor - ",v1.model_name)
'''


# Encapsulation:
class BankAccount:
    def __init__(self, owner, balance, pin):
        self.owner = owner
        print("Inside its own constructor", self.owner)
        self._balance = balance
        print("Inside its own constructor", self._balance)
        self.__pin = pin
        print("Inside its own constructor", self.__pin)

    def display(self):
        print("Inside the class", self.owner)
        print("Inside the class", self._balance)
        print("Inside the class", self.__pin)

class SavingsAccount(BankAccount):
    def __init__(self, owner, balance, pin, interest_rate):
        super().__init__(owner, balance, pin)
        self.interest_rate = interest_rate

    def access_parent_data(self):
        print("Owner:", self.owner)
        print("Balance:", self._balance)
        print("Balance:", self.__pin)

Sa = SavingsAccount("Ankit ETL QA LABS",145345,7365, 8.2)
Sa.access_parent_data()


'''
bank = BankAccount("Ankit ETL QA LABS",145345,7365)
bank.display()
print(bank.owner)
print(bank._balance #This should not be allowed
#print(bank.__pin)
'''


