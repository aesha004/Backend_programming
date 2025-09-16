# Lab task : add elements of list 
list = [5,1,8,9,2,5]
sum = 0
for i in list:
    sum = sum + i
print (f"Sum of all the elements in list is : {sum}")


#lab task - start and end range ask from user and sum_of_even and sum_of_odd numbers don't use increment/decrement
"""start = int(input("Enter start range value :"))
end = int(input("Enter end range value :"))
sum_even = 0
sum_odd = 0
for i in range (start,end + 1): # this end + 1 works like suppose start=100 & end=150 then by adding +1 it will include 150 number also
    if i % 2 == 0:
        sum_even = sum_even + i
    else:
       sum_odd = sum_odd + i
print("Sum of Even Numbers is : ",sum_even)
print("Sum of Odd Numbers is : ",sum_odd)  """


# sum of Numbers in range example
"""sum = 0
for i in range(1,11):
    sum  += i #sum = sum + i
print("Sum of 1 t0 10 numbers is :",sum)
"""

#lab task - print even start value and end value ask from user
"""start = int(input("Enter start range value :"))
end = int(input("Enter end range value :"))
for i in range(start,end,2):
    print(i)"""


# practice examples 
"""for _ in range(5):
    print("Hello")

for i in range(1,7):
    print("Bye",i)

my_list = ['Apple' , 'guava' , 'Cheery']
for fruits in my_list:
    print(fruits)

my_tuple = (1,"Bus" , 3 , "Car" , 4 , "Activa")
for vehicles in my_tuple:
    print(vehicles,end = " ")

for i in range(1,10,3):
    print("\n")
    print("Aesha",i)

for i in range(10,1,-1):
    print(i)
"""

# Multiplication Table Example
"""number = int(input("Enter a number :"))
for i in range (1,number+1):
    print(f"{number} * {i} = {number * i}")"""


#Factorial Example
"""number = int(input("Enter a number :"))
fact = 1
for i in range (1,number+1):
    fact *=  i
print(f"Factorial of {number} is : {fact}")"""