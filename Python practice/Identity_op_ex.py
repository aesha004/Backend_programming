a = [1,2,3]
b = [1,2,3]
c = a
name1 = "Aesha"
name2 = "Aesha"
print(a is b) #false
print(a is not b) #true because a and b have different memory locations
print(a is c) #true
print(a is not c) #false beacuase a and c have same memory locations
print(name1 is name2) #true
print(name1 is not name2) #false because name1 and name2 have same memory locations

print("id(a):",id(a))
print("id(c):",id(c))
print("id(b):",id(b))
print("id(name1):",id(name1))
print("id(name2):",id(name2))

#lab task ('is' and '==') operator difference
x = [2,3,4]
y = [2,3,4]
print("X is Y :" , x is y) #different memory locations
print("X == Y :" , x == y) #same values
