# String Slicing
# s[start:end:steps]
# steps can be +ve (let to right) or -ve (right to left pointer movement)
'''
s = "Banglore"
# Take out a sub-string of first 4 chars (index 0 to 3)
s1 = s[0:4:1]
print(s1)

# Take out a sub-string of last 4 chars (index 0 to 3)
end = len(s)
print(end)
start = end-4
s2 = s[start:end:1]
print(s2)

st = "Banglore"
l =len(st)
print("Length is:",l)
s = l-4
print("S is:",s)
e = l-1
print("E is:",e)
s2 = st[s:e-1:1]
print("S2 is:",s2)

# Print last 4 chars in reverse direction
print(s)
print(e)
print(st[e:s-1:-1])
#way 2
print(st[-1:e-4:-1])


st1 = "BANGALORECITY"
# Print from 4th (index:3) to 10th char (index : 9)
print(st1[3:10:1])
print(st1[4-1:9+1:1])

# Print fom 2nd last char(T:index:-2) to 4th last char(end index : -4)

print(st1[-2:-5:-1])
# Print whole reverse string
print(st1[::-1])

# print whole string
print(st1[::1])

# Print C in the name
print(st1[9])
print(st1[-4])

# Print me last char
print(st1[-1])

l = len(st1)
print("Length is:",l)
print(st1[l-1])
'''
# Q1 : Print the characters from the string
city = "Hyderabad"

# way 1 using extended (advanced for loop)
for ch in city:
    #print(ch)
    pass

# Way 2 using indexed for loop
le = len(city)
for idx in range(0,le,1):
    #print(city[idx])
    pass

# way 3 using while loop
s = 0
e = le-1
while(s<=e):
    #print(city[s])
    s = s+1
    pass

# Q2 : Reverse the string.
city = "Hyderabad"

# Way 1 using slicing
#print(city[::-1])

# way 2 using while loop
le = len(city) # 9
ei = le-1 # 8
ans = ""
while ei >=0:
    ans = ans + city[ei]
    ei=ei-1
print(ans)
