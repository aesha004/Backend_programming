my_dict = {
    "name": "Aesha",
    "age": 30,
    "city": "New York"
}
print(my_dict)

# 1. len() Method - find length of dictionary.
dict1 = { 1:"Ahmedabad" , 2:"Anand" , 3:"Surat" , "4":"Khambhat", 1:"Baroda"}
print(dict1)
print(f" Length of dictionary is : {len(dict1)}")

# 2. keys() Method - Returns a list containing the dictionary's keys.
key1 = dict1.keys()
print(f"Keys in dictionary is : {key1}")
print(f"Type : {type(key1)}")

# 3. values() Method - Returns a list of all the values in the dictionary.
value1 = dict1.values()
print(f"values in dictionary is : {value1}")
print(f"Type : {type(value1)}")

# 4. items() Method - Returns a list containing a tuple for each key value pair.
items1 = dict1.items()
print(f"Key-value pair : {items1}")
print(f"Type : {type(items1)}")


    
