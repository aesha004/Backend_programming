# Examples of indexing
set1 = {'Apple' , 'guava' , 'Mango' , 'Banana'}
# print(set1[2]) # typeError - as set does not support indexing.
lst = list(set1)
print(f"Printing set item by converting into list : {lst[2]}") #output may be varies everytime as set is unordered

# iterating through the set
for i in set1:
    print(f"Elements of set is : {i}")

# Checking for membership
if "Banana" in set1:
    print("Banana is in the set.")

# slicing examples
set2 = {1,3,2,5,4,6,8}
lst1 = list(set2)
sliced_lst1 = lst1[2:6]
sliced_set = set(sliced_lst1)
print(f"Original set2 : {set2}")
print(f"Sliced list : {sliced_lst1}")
print(f"Sliced set : {sliced_set}")