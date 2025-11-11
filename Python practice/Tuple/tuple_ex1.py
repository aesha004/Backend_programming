# 1. Count Method - returns number of times a specified value occurs in a tuple.
tpl_names = ('Aesha','Aarya','Aisha')
print(tpl_names.count('Aisha')) 

# 2. index Method - finds first occurrence of the specified value.
tpl_numbers = (1,9,3,9,8,7)
print(tpl_numbers.index(3))

# Basics of tuple
tpl_number = (10,9,8,7)
print(tpl_number)

tpl_no1 = 10,9,8,7
print(tpl_no1)

tpl_no2 = 11 # this is consider as integer only
print(tpl_no2)

tpl_no3 = 11, # by adding comma to single element it becomes tuple
print(tpl_no3)
print(type(tpl_no3)) # type function to check datatype

tpl_names = ('aesha')
print(type(tpl_names))