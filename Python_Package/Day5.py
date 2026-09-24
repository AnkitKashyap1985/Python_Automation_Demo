# Q1 Write a function that prints maximum number from the list.
# numbers = [1,5,7,99,10], O/P : 99
'''
def get_maximum(list1):
    max = list1[0]
    length = len(list1)
    for idx in range(1,length,1):
        if list1[idx] > max:
            max=list1[idx]
    print(max)

numbers = [1, 5, 7, 99, 10]
get_maximum(numbers)

# Q2 Write a function that prints maximum number from the list.
# numbers = [1,5,7,99,10], O/P : 99


def get_max(list1):
    max = list1[0]
    length = len(list1)
    for idx in range(1, length, 1):
        if list1[idx] > max:
            max = list1[idx]
    return max

numbers = [1, 5, 7, 99, 10]
ans = get_max(numbers)
print(ans+100)

# Q3. Write a script which return the list of Prime numbers using function
# prime numbers : having 2 factors (1 or number itself except 1)
# 2 => 2 % 1 ==0, 2%2 == 0 (1,2) Prime
# 3 => (1,3) Prime
# 4 => (1,2,4) Not a Prime number
# 9 => (1,3,9) Not a Prime number
# 1 => (1) Not a Prime number

# Get all Prime the Prime number between 2 to 20.

def getPrimeNumbers(min_num, max_num):
    primes = []
    for num in range(min_num, max_num+1):
        count = 0
        for num1 in range(1,num+1):
            if num % num1 == 0:
                count = count + 1
        if count == 2:
            primes.append(num)
    print(primes)

min_num = 2
max_num = 20
getPrimeNumbers(min_num, max_num)


# Strings

channel_name = "Ankit the Kaspi Kappa"
s_idx = 0
#print(channel_name[s_idx])
e_idx = len(channel_name)-1
#print(channel_name[e_idx])
sL_nun = 1
for idx in range(s_idx,e_idx+1):
    print(sL_nun," . ",channel_name[idx])
    sL_nun = sL_nun + 1

'''

channel_name = "ETL Qa Labs"
# String slicing
# get me first 3 char. from the string
#print(channel_name[0:3:2])

# Get me char. at 5 and 6 from the string
#print(channel_name[4:7:1])

# Get me char. at 0 and end from the string
#print(channel_name[::2])


print(channel_name.upper())
print(channel_name.lower())

print(channel_name.capitalize())
print(channel_name.replace("Labs","Company"))

print(channel_name.find("Labs"))
print(channel_name.count("L"))

ans_list = channel_name.split()
print(ans_list)

email = "etl.qa.labs@gmail.com"
print(email.split("@"))
print(email.split("."))