'''
# eno : ename
# Dictionary (called MAP in JAVA)
# Dictionary stores key and value pair
# Dictionary is unordered, mutable where key must be unique and immutable

eno = [1,2,3,4]
ename = ["Ajay","Vijay","Thomas"]
employees_details = {1:"Ajay",2:"Vijay",3:"Thomas",4:"Ajay"}
#print(employees_details)

# Get all the keys (eno)
for key in employees_details.keys():
    print(key)

# Get all the values (ename)
for val in employees_details.values():
        print(val)

 # Get all the keys, values (eno, ename) - item
for item in employees_details.items():
        print(item," : ",type(item))

employees_details = {1:"Ajay",2:"Vijay",3:"Thomas",4:"Ajay"}
for k, v in employees_details.items():
    print(k," : ",v)

# to get a value
---------------------------------





# Function contains a block of code to put together
# It supports modularization

# Defining a function and executing it

def display():...
print("1")
print("2")
print("3")
print("4")

display()
display()
display()
display()

# Function that returns the value
def print_name():...
ans = print_name()
print(ans)
'''

# Why set is faster than list and tuple?
# Hash table

eno_list = [1,2,3,4]
eno_set = {1,2,3,4}
print(hash("ETL"))

