# 1. Append Method - adds an element to the end of the list here index value of new added list will be continued from first list
lst1 = [12,34,56,84]
print(f"Original List : {lst1}")

lst1.append(900)
print(f"After appending : {lst1}")

lst2 = [1,2,3,4,5]
lst1.append(lst2)
print(f"After append lst2 into lst1 : {lst1}")
print(f"Whole appended list2 have single index number : {lst1[5]}")


# 2. Extend Method - adds specified elements to end of current list but index value of every elements will be unique 
"""list1 = ['Anand' , 'Baroda' , 'Rajkot']
list2 = ['Khambhat','Petlad']
list1.extend(list2)
print(f"Extending list1 : {list1}")
print(f"Fourth index element : {list1[3]}")"""


# Difference Between Append and Extend
"""list1 = ['Anand' , 'Baroda' , 'Rajkot']
list2 = ['Khambhat','Petlad']
# list1.append(list2)
# print(f"Append use : {list1}")
# print(f"Access whole appended list1 : {list1[3]}")
list1.extend(list2)
print(f"Extend use : {list1}")
print(f"Access single element from list1 : {list1[3]}")"""


# 3. Clear Method - clears all the elements in the list
"""list = [89.90 , 'Aesha' , 'Riya' , 89]
list.clear()
print(f"Cleared list is : {list}")
# Delete keyword  use 
# del list # deletes whole list
# del list[2] # deletes 2nd index element from list
# print(list)"""

# 4. Copy Method - returns a copy of the specified list
list = [12 , 1 , 20.12 , 'Aesha' ]
new_list = list.copy() 
print(f"Copied List : {new_list} Original List : {list}")

new_list.append(9)
print("After appending using copy ")
print(f"Copied List : {new_list}  Original List : {list}")

# Difference between "="operator and "copy"function 

print("With the use of = operator")
new_list = list
print(f"Copied List : {new_list} Original List : {list}")
new_list.append(10)
print("After appending using = operator ")
print(f"Copied List : {new_list}  Original List : {list}")

# Simple example of list
"""lst = [1,23.56,'Aesha',45]
print(lst)
for i in lst:
    print(i,type(i))"""

# Lab task :-  Sum of all integer elements in list 
"""sum = 0
list = [1,2,67,'Aesha',89,12]
for i in list:
    if type(i) == int:
        sum  = sum + i
print(f"Sum of all integer elements in list is : {sum}")"""
