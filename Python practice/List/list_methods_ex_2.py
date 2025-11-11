# 5. Count Method - returns the number of elements with the specified value 
list = [1,2,5,8,9,5,6,5,'Aesha']
print(f"Total occurrences of 5 is : {list.count(5)}")
print(f"Total occurrences of Aesha is : {list.count('Aesha')} ")
print(f"Total occurrences of test is : {list.count('test')}")

# 6. index Method - returns the position at the first occurrence of the specified value.
print(f"Index value of first occurrence of 5 is : {list.index(5)}")
print(f"Index value of 5 between 6 to 8 is : {list.index(5,6,8)}")

# 7. insert Method - inserts the specified value at the specified position.
list.insert(2,'Patel')
print(f"Inserted value at index 2nd : {list}") 

# 8. pop Method - removes the element at the specified position.
"""print(f"Actual list : {list} ")
print(list.pop())
print(list.pop())
print(list.pop())
print(list.pop(2))
print(f"List after popping elements : {list}")"""

# 9. remove Method - removes the first occurrence of the element with the specified value.
"""print(f"Before Remove list : {list}")
list.remove(5)
print(f"After Remove list : {list}")"""
#list.remove(10) # valueError as value is not there 

# 10. reverse Method - reverses the elements of list.
list.reverse()
print(f"printing reverse list : {list}")

# 11. sort Method - sort the list in ascending order by default
my_list = ['heer' , 'prita' , 'ziya' , 'Aesha' , 'zoya']
my_list.sort(reverse = True) # true means decending order
print(f"Sorted list in Descending : {my_list}")
my_list.sort(reverse = False) # ascending order
print(f"Sorted list in Ascending : {my_list}")
my_list.sort(key = len)
print(f"Sorted list according to length : {my_list}")

numbers = [5, 3, 8, 1, 2]
numbers.sort()
print("After sort():", numbers)
numbers2 = [5, 3, 8, 1, 2]
sorted_list = sorted(numbers2)
print("After sorted():", sorted_list)
numbers.reverse()
print("After reverse() : ",numbers)
