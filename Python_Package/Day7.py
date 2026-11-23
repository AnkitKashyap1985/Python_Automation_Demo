'''
# 'a' => 97 "z" => 122
# "A" => 65 and
print (ord("a"))

print (chr(92))

print (bin(ord("अ")))


# Q3. Get me the sum of ASCII values of a given string
s1 = "abc"
sum = 0
for ch in s1:
    sum = sum + ord(ch)
print(sum)

print (ord("a"))


# Q4. Determine if my string contains lowercase char. or not
# name = "ETL QA LaBS"

def check_if_string_contains_lowercase(string_name):
    for ch in string_name:
        num = ord(ch)
        if (num >= 97 and num <= 122):
            return True
    return False

name = "ETL QA LABs"
ans = check_if_string_contains_lowercase(name)
print(ans)


# Q5. How to reverse words in a string.
# s1 = 'etl qa labs' , o/p : labs qa etl
s1 = 'etl qa labs'

# Way 1 using split function
list1 = s1.split(" ")
print(list1)
ans = ""
len1 = len(list1)

for idx in range (len1-1,-1,-1):
    ans = ans +" "+ list1[idx]
print(ans)

# Way 2 using while loop (H.W)

'''
# Way 3 : Using string slicing with split
s1 = 'etl qa labs'
list1 = s1.split(" ")
#print(list1)
revlist = list1 [::-1]
#print(revlist)
ans = ""
for ele in revlist:
    ans = ans +" "+ ele
print(ans)

ans_join = " ".join(revlist)
print(ans_join)


# Q6. Return a substring which starts with Q and ends with B
# s1 = "ETLQALABS" O/P => QALAB
s1 = "ETLQALABS"
start = s1.find('Q')
end = s1.find('B')
ans = s1[start:end+1:1]
print(ans)
'''

# Q7. Count the number of occurrence of the each element int he list
# list1 = [1,2,3,4,5,1,2,5,5]
# O/P : {1:2,2:2,3:1,4:1,5:3}

def count_list_occurrences(list1):
    count_element={}
    for ele in list1:
        if ele in count_element:
            count_element[ele]=count_element[ele]+1
        else:
            count_element[ele]=1
    return count_element

list1 = [1,2,3,4,5,1,2,5,5]
ans = count_list_occurrences(list1)
print(ans)


# Q8: Get me all the duplicate numbers from the list

def getDuplicate(ans):
    duplicateList=[]
    for key in ans.keys():
        if ans[key]>1:
            duplicateList.append(key)
    return duplicateList
print(getDuplicate(ans))

# Q9: Get me all the unique numbers from the list

def getUnique(ans):
    uniqueList=[]
    for key in ans.keys():
        if ans[key]==1:
            uniqueList.append(key)
    return uniqueList
print(getUnique(ans))

# Get the count of each elements without using dictionary.
list1 = [1,2,3,4,5,1,2,5,5]
duplicate_set = set()
for ele in list1:
    if list1.count(ele)>1 and ele not in duplicate_set:
        duplicate_set.append(ele)
        duplicate_set.add(ele)'''