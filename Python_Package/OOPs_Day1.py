# Print "Hello" 10 times

# Procedural way
'''
print("Hello")
print("Hello")
print("Hello")
print("Hello")
print("Hello")
print("Hello")
print("Hello")
print("Hello")
print("Hello")
print("Hello")
print("Good Bye")


# Functional way

def Print_hello():
    print("Hello")
    print("Hello")
    print("Hello")
    print("Hello")
    print("Hello")
    print("Hello")
    print("Hello")
    print("Hello")
    print("Hello")
    print("Hello")

def print_bye():
    print("Good Bye")

Print_hello()
Print_hello()
Print_bye()
'''
# Object oriented programming way

class PrintClass:
    name = "ETL QA Labs"
    def print_hello(self):
        print("Hello")
        print("Hello")
        print("Hello")
        print("Hello")
        print("Hello")

    def print_bye(self):
        print("Good Bye")


#PrintClass().print_hello()
#PrintClass().print_bye()

# Create Object

obj1 = PrintClass()
obj1.print_hello()
obj1.print_bye()
print(obj1.name)

print(type(obj1))

name ="ETL"
print(type(name))
age = 41
print(type(age))

