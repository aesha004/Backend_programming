# 1. Write a function that accepts a list of numbers and returns the average of the numbers.
"""def find_avg(list):
    total = sum(list)
    avg = total / len(list)
    return avg

input_num =int(input("How many numbers you want in list : "))
list = []
for i in range(input_num):
    user_input= int(input(f"Enter Number {i + 1} : "))
    list.append(user_input)

print(f"List of Numbers : {list}")

print(f"Average of Numbers in list is : {find_avg(list)}")"""
    

# 2. Accept a string from the user and print it in uppercase if the length of the string is greater than 5, else print it in lowercase using a function.
"""def checkstring (string):
    if len(string) > 5 :
        print(f"String in uppercase : {string.upper()}")
    else:
        print(f"String in lowercase : {string.lower()}")

string = input("Enter a string : ")
checkstring(string)"""


# 3. Write a function that accepts a list of numbers and returns a new list with only the numbers that are divisible by 3.
'''def check_div_3(list):
    new_list = []
    for i in list :
        if i % 3 == 0:
            new_list.append(i)
    return new_list

# input section 
input_num =int(input("How many numbers you want in list : "))
list = []
for i in range(input_num):
    user_input= int(input(f"Enter Number {i + 1} : "))
    list.append(user_input)

print("List of Numbers : ",list)

# function calling
new_list = check_div_3(list)
print(f"Numbers divisible by 3 : {new_list}")'''


# 4. Write a function that accepts a list of numbers and returns a new list with the squares of all the numbers in the list.
'''def sqr_num(list):
    sqr_list = [i ** 2 for i in list] # using list comprehension
    return sqr_list

# input section 
input_num =int(input("How many numbers you want in list : "))
list = []
for i in range(input_num):
    user_input= int(input(f"Enter Number {i + 1} : "))
    list.append(user_input)

print("Original List of Numbers : ",list)

# function calling 
sqr_list = sqr_num(list)
print(f"Squares of Numbers List : {sqr_list}")'''


# 5. Write a function that accepts a string and counts how many vowels are in the string.
'''def vowel_count(string):
    vowels = 0
    for i in range(len(string)):
        if string[i] in 'aeiouAEIOU':
            vowels += 1
    return vowels    

string = input("Enter a string : ")
vowels = vowel_count(string)
print(f"Total number of vowels present in string is : {vowels} ")'''


# 6. Write a function that accepts a list of strings and returns the longest string in the list.
list_str = ["Aesha","Heer","Aisha","Hitesh"]
def check_str(list_str):
    largest = list_str[0]
    for words in list_str:
        if len(words) > len(largest):
            largest = words   
    return largest

largest = check_str(list_str) 
print(f"Largest string in list is : {largest}")


# 7. Write a function that accepts a number and checks if it is an Armstrong number.
num = int(input("Enter a number : "))
def armstrong_num(num):
    digits = str(num)    # Convert number to string to get number of digits

    temp = num
    sum = 0
    while (temp > 0):
        remainder = temp % 10         # Get last digit
        power = remainder ** len(digits) # Raise it to the number of digits
        sum += power    # Add to total
        temp = temp // 10  # Remove last digit
 
    if num == sum:
        print(f"{num} is a amstrong number. ")
    else:
        print(f"{num} is not a amstrong number. ")

armstrong_num(num)


# 8. Write a function that accepts a number and returns the sum of its digits.















# 9. Write a function that accepts a string and returns the string in alternating uppercase and lowercase characters.












# 10. Write a function that accepts a list of strings and returns a new list with only the strings that have an odd length.
























