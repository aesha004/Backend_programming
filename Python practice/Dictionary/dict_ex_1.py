# accessing items from dict
dict = {1:"Anand" , 2:"Khambhat" , 3:"Surat" , 4:"Baroda"}
for key in dict.keys():
    print(f"{key} - key")

for value in dict.values():
    print(f"{value} - value")

for k,v in dict.items():
    print(f"{k} --> {v}")

# filtering of dictionary acc to different conditions.
dict1 = { 101: ['Aesha', 'parimal','python',8900],
          102: ['Heer' , 'Cg road', 'se' , 7800],
          103: ['Aisha' , 'sg road' , 'java' ,2300],
          104: ['Aarya' , 'Chakdol ground' , 'Data science' ,8000]
        }
for key,value in dict1.items():
    if value[3] > 2300:
        print(key)
        for i in value:
            print(f"\t{i}")

# output  ans= ('dhruv',240),('Roamil',247)
dict1 = { 101: ['Aesha', 'parimal','python',89,45,70],
          102: ['Heer' , 'Cg road', 'se' ,40,23,45],
          103: ['Aisha' , 'sg road' , 'java' ,23,60,20],
          104: ['Aarya' , 'Chakdol ground' , 'Data science' ,80,78,90]
        }
ans = [] # to store tuple items
for value in dict1.values():
    name = value[0]           # student's name
    total = sum(value[3:])    # total marks
    ans.append((name,total))  # stores in tuple
ans = tuple(ans) # convert list to tuple
print(f"ans = {ans}")

# acess particular value using key 
print(dict1[101][2])  # python

# Access items through key
dict1 = {
    "1" : "One",
    "2" : "Two",
    "3" : "Three"
}
print(f"Access value through specified key : {dict1["2"]}")

# Add item in dictionary
dict1[4] = "Four"
print(f"Added item in dictionary : {dict1}")

# Update item in dictionary
dict1["2"] = "Twenty Two"
print(f"Updated item in dictionary : {dict1}")

# delete particular item & dictionary
del dict1["3"]
print(dict1)

# del dict1
# print(dict1)

# Fetch subjects using keys and value
dict3 = {
    101: ['Aesha', 'parimal','python',8900],
    102: ['Heer' , 'Cg road', 'se' , 7800],
    103: ['Aisha' , 'sg road' , 'java' ,2300],
    104: ['Aarya' , 'Chakdol ground' , 'Data science' ,8000]
}
for i in dict3.keys():
    print(f" {dict3[i][2]}")

# for j in dict3.values():
#     print(f"{j} - {j[2]}")