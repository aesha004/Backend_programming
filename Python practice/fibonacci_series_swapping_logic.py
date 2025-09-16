# Fibonacci using "for loop"
number = int(input("Enter a number: "))
sum = 0
previous = 0
next = 1
for i in range(number):
    if i == 0:
        sum = 0  # this because first number in series is 0 itself 
    else:
        previous = next
        next = sum
        sum = previous + next
    print(sum,end = " ")
    

# Fibonacci using "While loop"
number = int(input("Enter a number: "))
sum = 0
previous = 0
next = 1
i = 0
while (i<=number):
    if i==0:
        sum = 0
    else:
        previous = next
        next = sum
        sum = previous + next
    i+=1
    print(sum , end =" ")


# swapping two numbers using third variable
number1 = int(input("Enter a number1: "))
number2 = int(input("Enter a number2: "))
temp = number1
#print(f"{temp} = {number1}")
number1 = number2
#print(f"{number1} = {number2}")
number2 = temp
#print(f"{number2} = {temp}")
print(f"After swapping number1 is {number1} and number2 is {number2} ")


# Again swapping using python functionalities only python supports this logic(easiest way for swapping)
number1 = int(input("Enter a number1: "))
number2 = int(input("Enter a number2: "))
number1 , number2 = number2 , number1
print(f"After swapping number1 is {number1} and number2 is {number2} ")


# Fibonacci using shortcut swapping logic  
number = int(input("Enter a number: "))
previous = 0 # first number of series
next = 1 # 2nd number of series
for i in range (number):
    print(previous , end = " ")   # put this line before main line reason is to first print series start from "0" 
    previous , next = next , previous + next
    # print(previous , end = " ") and if i write here than it will always start from "1" and not 0.

