# normal way
lst1 = [1,2,3,4]
lst2 = []
for i in lst1:
    lst2.append(i)
print(lst2)

# Comprehension way
lst1 = [1,2,3,4]
lst2 = [i for i in lst1]
print(lst2)

# want square of each element in lst2
lst1 = [1,2,3,4]
lst2 = [i*i for i in lst1]
print(lst2)

# want square of even numbers in list
lst_even = [2,1,3,4]
lst_new_even = [i*i for i in lst_even if i%2==0]
print(lst_new_even)

# if list = [1,2,3] i want output like this :- [(1,1,1) , (2,4,8) , (3,9,27)]
sum = 0
list = [1,2,3]
lst_new = [(i,i*i,i**3) for i in list]
print(lst_new)
for i in lst_new:
    sum = sum +i[1]
print(f"Sum of middle numbers : {sum}")

# want to convert  string into upper case whose length is more than 8 
lst_string = ['khambhat' , 'baroda' , 'ahmedabad' , 'surat']
upper_lst = [i.upper() for i in lst_string if len(i) >= 8 ]
print(upper_lst)