# Control Statement: manage the flow of execution of your program
'''
age = 15
# if statement
if age >= 18:
    print("You are old enough to vote")
print("Ok lets go")



age = 15
# if.... else statement
if age >= 18:
    print("You are old enough to vote")
else:
    print("You are NOT old enough to vote")
print("Khatam")

age = int(input("Enter your age: "))
# Elif statement
if age > 18:
    print("You are old enough to vote")
elif age == 18:
    print("You are STILL NOT old enough to vote")
else:
    print("You are NOT old enough to vote")
print("Khatam")



# Looping Statement
# for and while loop
# range(20) => 0,1,2,3......,19, starts with 0 and ends with number-1
# range(start_value, end_value, steps), range(1,20,2) => 1,3,5,7......19
# range(2,20,3) => 2,5,8,11,14,17

# for loop
for age in range(10):
    print(age)
    `
name = "Ankit"
if name:
    print("True")
else:
    print("False")


# for loop
# range(20) ~ range(0,10,1)
for num in range(10):
    print(num)'

# print all the even number starting from 2
for num in range(2,20,2):
    print(num)

# print all the odd number till 20 starting from 1
for num in range(1,20,2):
    print(num)

# While loop stops after evalution of a condition as False
# print 1 to 10

start_val = 1
end_val = 10

while start_val <= end_val:
    print(start_val)
    start_val = start_val + 1

x = True
y = False

# Logical operation
ans1 = x and y
ans2 = x or y
print (x and y)
print (x or y)


# Q1. Record count validation between source and target
source_count = 1000
target_count = 980
if source_count == target_count:
    print("PASS - Source and target are equal")
else:
    print("Fail - Source and target are not equal")
    missing_count = source_count - target_count
    print("Missing record counts:", missing_count)


# Q2. ETL job SLA validation, Job should be completed within 30mins
# a) 30 min/less -> SLA met
# b) 31-45 mins -> SLA warning
# c) more than 45 mins -> SLA breached

duration = 50
if duration <= 30:
    print("SLA met")
elif duration <= 45:
    print("SLA Warning!!!")
else:
    print("SLA Breached!!!")


# Q3. Validate 10 ETL records
for record in range(1,11):
    print("Validating record", record)
print("Validation Completed")



# Q4. Identify failed ETl records
# 20 records and I want to print every 5th record the failed record
# 1....20 => 5,10,15,20

for i in range(1,30,1):
    if i % 5 == 0:
        print("Failed records:",i)
 '''

# Q2. ETL job SLA validation, Job should be completed within 30mins
# a) 30 min/less -> SLA met
# b) 31-45 mins -> SLA warning
# c) more than 45 mins -> SLA breached

duration = 44.5
if duration <= 30:
    print("SLA met")
elif duration <= 45:
    print("SLA Warning!!!")
else:
    print("SLA Breached!!!")

