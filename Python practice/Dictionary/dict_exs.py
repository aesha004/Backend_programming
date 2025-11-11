# Accessing, adding, updating, and deleting dictionary elements. 
student = {"name": "Aesha", "age": 20, "course": "Python"}
print("Original dictionary:", student)
print("Name:", student["name"])
student["city"] = "Mumbai"
print("After adding city:", student)
student["age"] = 21
print("After updating age:", student)
del student["course"]
print("After deleting course:", student)

# Create a dictionary with 6 key-value pairs
student = {
    "name": "Aesha",
    "age": 20,
    "course": "Python",
    "city": "Mumbai",
    "grade": "A",
    "college": "MBIT"
}
print("Student Dictionary:")
print(student)
# Access values using keys
print("Name:", student["name"])
print("Age:", student["age"])
print("Course:", student["course"])
print("City:", student["city"])

# Merging two lists into a dictionary using zip(). 
keys = ["name", "age", "city"]
values = ["Aesha", 20, "Mumbai"]
my_dict = dict(zip(keys, values))
print("Dictionary using zip():", my_dict)

# using loop
keys = ["name", "age", "city"]
values = ["Aesha", 20, "Mumbai"]
my_dict = {}
for i in range(len(keys)):
    my_dict[keys[i]] = values[i]
print("Dictionary using loop:", my_dict)


# Counting occurrences of characters in a string using dictionaries. 
string = input("Enter a string : ")
dict = {}
for char in string:
    if char in dict:
        dict[char] += 1
    else:
        dict[char] = 1

print("Character counts:")
for key, value in dict.items():
    print(f"{key} : {value}")
