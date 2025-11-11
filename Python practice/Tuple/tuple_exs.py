tuple = (12,20,30,50,80,100,90)
print("Value from the last index : ",tuple[-1])
print("Values between index 1 and 5 : ",tuple[1:5])
print("Alternate Values between index 1 and 5 : ",tuple[1:6:2])
print("Value at first index : ",tuple[1])


# Write a Python program to convert a list into a tuple. 
"""my_list = [10, 20, 30, 40, 50]
# Convert list to tuple
my_tuple = tuple(my_list)
print("List:", my_list)
print("Tuple:", my_tuple)
"""

# Creating and accessing elements in a tuple.
fruits = ('apple', 'banana', 'cherry')
print("All fruits:", fruits)
print("First fruit:", fruits[0])      # Access by index
print("Last fruit:", fruits[-1])      # Negative index

# Basic operations with tuples: concatenation, repetition, membership.
t1 = (1, 2, 3)
t2 = (4, 5)
print("Concatenation:", t1 + t2)
print("Repetition:", t1 * 2)
print("Is 2 in t1?", 2 in t1)
print("Is 6 not in t1?", 6 not in t1)
