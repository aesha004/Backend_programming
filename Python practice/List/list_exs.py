# Python program to access elements at different index positions
fruits = ["Apple", "Banana", "Cherry", "Mango", "Orange"]
print("List of fruits:", fruits)

print("\nAccessing elements at different positions:")
print("Element at index 0:", fruits[0])
print("Element at index 2:", fruits[2])
print("Element at index 4:", fruits[4])

print("\nAccessing elements using negative indexes:")
print("Last element (index -1):", fruits[-1])
print("Second last element (index -2):", fruits[-2])

# Write a Python program to create a list with elements of multiple data types (integers, strings, floats, etc.). 
list = [12,"Hiya",12.30]
print("List having multiple data types :" ,list)

# Write a Python program to find the length of a list using the len() function.
list = [12,"hiya" , 12.30]
print("Length of list is : ",len(list))

# Python program to remove elements from a list using pop() and remove()
fruits = ["apple", "banana", "cherry", "mango", "orange"]
print("Original list:", fruits)
fruits.remove("banana")
print("After using remove('banana'):", fruits)
removed_item = fruits.pop(2)   # removes element at index 2
print("Element removed using pop():", removed_item)
print("List after using pop():", fruits)

# Write a Python program to insert elements into an empty list using a for loop and append().
list = []
for i in range(3):
    element = input("Enter a element : ")
    list.append(element)
print("Final list ",list)

# Basic list manipulations: addition, deletion, updating, and slicing. 
fruits = ['apple', 'banana', 'cherry']
print("Original list:", fruits)
fruits.append('mango')
print("After addition:", fruits)
fruits.remove('banana')
print("After deletion:", fruits)
fruits[1] = 'orange'
print("After updating:", fruits)
print("Sliced list (first two elements):", fruits[0:2])
