# Write a program to remove all items from a list that are less then 5 e.g [12,3,4,5,67,0] output [12,67,5]
list = [12,3,4,5,67,0]
list_new = [i for i in list if i >= 5 ]
print(f"List after removing number less than 5 is : {list_new}")
    
# Write a program to find common among 2 lists. eg. lst_numbers = [1,2,34,33,21] lst_numbers2=[11,2,33,45] output [2,33]
lst_num1 = [1,2,34,33,21]
lst_num2 = [11,2,33,45]
new_list_num = []
for i in lst_num1:
    for j in lst_num2:
        if i == j:
            new_list_num.append(i)
print(f"Common among two list is : {new_list_num}")

# Write a program to sort a list of strings by their length e.g ['apple', 'banana', 'kiwi', 'orange'] output : ['kiwi', 'apple', 'banana' , 'orange']
lst_fruits = ['apple', 'banana', 'kiwi', 'orange']
lst_fruits.sort(key = len)
print(f"Sorted fruits acc to length : {lst_fruits}")

# Write a program to accepts a list of integers and returns a tuple with the sum of all positive numbers and the sum of all negative numbers.
"""user_input = int(input("Enter how many integer values you want in list : "))
list = []
for i in range(user_input):
    list.append(int(input("Enter integer values : ")))
print(f"List of integers : {list}")

sum_positive = 0
sum_negative = 0
tuple = ()
for i in list:
    if i > 0:
        sum_positive = sum_positive + i
    elif i < 0:
        sum_negative = sum_negative + i 
result = (sum_positive , sum_negative )
print(f"Sum of positive and negative numbers in tuple : {result}")"""

# Write a program that takes a list of numbers and returns a tuple containing the sum and product of all the numbers.
# Input: `[1, 2, 3, 4]`
# Output: `(10, 24)`
user_input1 = int(input("Enter how many integer values you want in list : "))
list1 = []
for i in range(user_input1):
    list1.append(int(input("Enter numbers : ")))
print(f"List of numbers : {list1}")

sum  = 0
mul = 1
for i in list1:
    sum = sum + i
    # print(f"{sum} = {sum} + {i}")
    mul = mul * i
    # print(f"{mul} = {mul} * {i}")
result = (sum , mul)
print(result)
print(f"Sum and Product of numbers present in list is : {result}")
