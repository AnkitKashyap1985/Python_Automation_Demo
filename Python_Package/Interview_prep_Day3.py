# Find all the duplicates elements from the list return all the duplicates
'''

list=[1,2,3,4,51,2,3,5,6,7,8,9]
# O/P: [1,2,3]

def get_dupes(list):
    duplicate_list=[]
    for i in range (0,len(list)): # i = 0 to (12-1), 1
        for j in range (i+1,len(list)): # j = i+1 to (12-1)
            if list[i]==list[j]:
                if list[i] not in duplicate_list:
                    duplicate_list.append(list[i]) # [1,2,3]
    return duplicate_list

ans=get_dupes(list)
print(ans)

# TC = O(n*n)
# SC = O(1)


#Approach 2 using set

def find_duplicates(list):
    seen = set()
    duplicates = set()

    for ele in list:
        if ele in seen: # seen = {1,2,3,4,5,6,7,8,9}
            duplicates.add(ele) # duplicates = {1,2,3}
        else:
            seen.add(ele)
    return duplicates

list=[1,2,3,4,51,2,3,5,6,7,8,9]
ans = find_duplicates(list)
print(ans)

# TC = O(n)
# SC = O(n)


# Charachter Frequency

# Approach 1

#text = "etl qa labs"
#O/P = {"e":1,"e":1,"1":2......}

# Use dictionary
text = "etl qa labs"
def get_char_freq(text):
    freq = {}              # freq = {"e":1,"t":1,"l":2," ":2,"q":1,"a":1}
    for char in text:
        if char in freq:
            freq[char] = freq[char] + 1
        else:
            freq[char] = 1
    return freq
ans = get_char_freq(text)
print(ans)

#TC = O(n)
#SC = O(1)
'''

# Approach 2

text = "etl qa llabs"

#print(text.count("l"))
def get_char_freq_usingCount(text):
    freq = {}
    for char in text:
        freq[char] = text.count(char)

    return freq
ans = get_char_freq_usingCount(text)
print(ans)

#TC = O(n)
#SC = O(1)