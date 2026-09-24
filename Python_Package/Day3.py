'''
# Primitive datatype

name_list = ["Ram", "Shyam", "Ghanshyam",25,20,40]
print("Original_list :",name_list,":    :",type(name_list))
name_list.append("Thomas")
print("Updated_list :",name_list,":    :",type(name_list))


name_list=["Ram", "Shyam", "Ghanshyam"]
print(name_list[0])
print(name_list[1])

name_list.remove("Shyam")
print(name_list[0])
print(name_list[1])


name_list = ["Ram", "Shyam", "Ghanshyam", "Thomas", "Ali"]
print(name_list)

#print(name_list[0])
#print(name_list[4])
#print(name_list[3])
#print(name_list[2])
#print(name_list[1])

# using FOR loop
# Way 1
for idx in range(2,5,1):
    print("Hello:",name_list[idx])

# way 2
for item in name_list:
    print("Hello :",item,"How are you?")


# Create a smaller list from 3rd(end index)to 5th item in the list

ans_list = []
for idx in range(2,5,1):
    print("Hello:",name_list[idx])
    ans_list.append(name_list[idx])
print("Answer list :",ans_list)

from typing import Tuple

# Tuple " An ordered collection of items that can NOT be changed (immutable)
# you can store different type of data in a tuple

# Ordered : Insertion order preserved
# Immutable : can NOT add or remove some items from the tuple

name_tuple = ("Ram", "Shyam", "Ghanshyam", 25,20,40)
print("Tuple is :", name_tuple, "and data type is :", type(name_tuple))
# Fstring way of printing
print(f"Tuple is : {name_tuple} and data type is : {type(name_tuple)}")


# Set : an Un-ordered collection of unique items (Set doesn't allow duplicates) and its mutable
name_tuple = ("Ram", "Shyam", "Ghanshyam", "Ram")
#print(name_tuple)

name_set = {"Ram", "Shyam", "Ghanshyam", "Ram"}
#print(f"Set is : {name_set} and data type is : {type(name_set)}")

# XXXprint(name_set[0])XXX
name_set.add("Mohan")
print(name_set)

# Print all the element from the set
for item in name_set:
    print("Hello",item,"How are you?")
'''

# Special method applicable to set
# Union, intersection, difference(minus/except)

num1_set = {1,2,3,4}
num2_set = {5,6,3,7}

# Union (| (or))
ans = num1_set | num2_set
print("Answer is : ",ans," and type is :",type(ans))
ans = num1_set & num2_set
print("Answer is : ",ans," and type is :",type(ans))
ans = num1_set.union (num2_set)
print("Answer is : ",ans," and type is :",type(ans))



# Difference (-(minus))
ans = num1_set- (num2_set)
print("Difference Operator:",ans)
ans = num1_set.difference (num2_set)
print("Answer is : ",ans," and type is :",type(ans))