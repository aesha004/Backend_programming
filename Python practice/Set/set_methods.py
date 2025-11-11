# 1. Add() Method - adds an element to the set. 
set_num = {1,30,3,2,9}
print(set_num)
set_num.add("test")
print(f"Add Method : {set_num}")

# 2. clear() Method - Removes all the elements from the set.
set_num.clear()
print(f"Clear Method : {set_num}")

# 3. copy() Method - Returns a copy of the set.
set_num = {12,10,13,15}
set_num1 = set_num.copy()
print(f"Copy Method : {set_num1}")

# 4. difference() Method - returns a set that contains the difference between two sets.
# The returned set contains items that exist only in the first set, and not in both sets.
set_num1 = {1,2,3,23,45}
set_num2 = {1,2,9,67}
print(f"Set 1 : {set_num1}")
print(f"Set 2 : {set_num2}")
ans = set_num1.difference(set_num2)
print(f"Difference of set1 and set2 is : {ans}")

ans = set_num2.difference(set_num1)
print(f"Difference of set2 and set1 is : {ans}")

# 5. union() Method - returns a set that contains all items from the original set.
ans = set_num1.union(set_num2)
print(f"Union of set1 and set2 is : {ans}")

# 6. intersection() Method - returns a set that contains the similarity between two or more sets.
ans = set_num1.intersection(set_num2)
print(f"Intersection of set1 and set2 is : {ans}")

# 7. symmetric-difference() Method - returns all the uncommon items from both the sets and all the common items are not included.
ans = set_num1.symmetric_difference(set_num2)
print(f"Symmetric Difference of set1 and set2 is : {ans} ") 

# 8. issubset() Method - returns boolean value true if all items in the set exists in specified set , otherwise it returns false.
set1 = {1,2,5,3,4,6}
set2 = {2,3,4}
print(f"set2 is subset of set1 (set2 all items present in set1) : {set2.issubset(set1)}")
print(f"set1 is not subset of set2 (set1 all items not present in set2) : {set1.issubset(set2)}")