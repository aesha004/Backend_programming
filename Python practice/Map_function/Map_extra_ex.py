# 1. Write a Python program that uses the `map()` function to square each number in a given list of integers. 
# Input: [1, 2, 3, 4] , Output: [1, 4, 9, 16]
def square(num):
    return num * num

lst_numbers = [1,2,3,4]
lst_sqr = list(map(square,lst_numbers))
print(f"Square of each Number is : {lst_sqr}")


# 2. Write a Python program that uses `map()` to convert a list of strings to uppercase. 
# Input: ['apple', 'banana', 'cherry'] - Output: ['APPLE', 'BANANA', 'CHERRY']
lst_fruits = ['Apple' , 'Banana' , 'Cherry']
lst_upper = list(map(str.upper,lst_fruits))
print(f"List of string in uppercase : {lst_upper}")
    

# 3. Write a Python program that uses `map()` to find the length of each string in a list of strings. 
# Input: ['hello', 'world', 'python'] Output: [5, 5, 6]
lst_str = ['hello' , 'world' , 'python']
lst_len = list(map(len,lst_str))
print(f"Length of items in list : {lst_len}")


# 4. Write a Python program that uses `map()` to add a given number to each element in a list.  
# Input: [1, 2, 3, 4] , 5 Output: [6, 7, 8, 9]
def add_num(num):
    num1 = num + 5
    return num1

lst_numbers = [1,2,3,4]
lst_added_numbers = list(map(add_num,lst_numbers))
print(f"After Added Number 5 in list : {lst_added_numbers}")


# 5. Write a Python program that uses `map()` to apply a function that converts a list of temperature values in Celsius to Fahrenheit. 
# Input: [0, 25, 100] Output: [32.0, 77.0, 212.0]
lst_temp = [0,25,100]
def convert_temp(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

lst_fah = list(map(convert_temp,lst_temp))
print(f"List of temperature values in Celsius to Fahrenheit : {lst_fah}")

