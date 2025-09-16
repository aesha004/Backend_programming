# nested if example 
age = int(input("Enter your Age : "))
weight = int(input("Enter your Weight : "))
if age > 18 :
    if weight > 55:
        print("You are eligible to donate blood ")
    else :
        print("You cannot donate blood due to under weight ")
else :
    print("You cannot donate blood due to under age ")


# also done using simple if-else
""" age = int(input("Enter your Age : "))
weight = int(input("Enter your Weight : "))
if age > 18 and weight > 55:
    print("You are eligible to donate blood ")
else :
    print("You are not eligible ")
"""

# Program to check greater, less, or equal using if-else
"""num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
if num1 > num2:
    print(f"{num1} is greater than {num2}")
else :
    print(f"{num1} is less than {num2}")
"""

# program to check prime number or not using if-else
# num = int(input("Enter a number: "))
# if num > 1:
#     for i in range(2,num):
#         if (num % i) == 0:
#             print(f"{num} is not a prime number")
#             break
#         else:
#             print(f"{num} is a prime number")


# if-else statement example
"""age = int(input("Enter your age: "))
if age >= 18:
    print("You are an adult.")
else:
    print("You are a minor.")
"""

# if-elif-else statement example
marks = int(input("Enter your marks: "))
if marks >= 70:
    print("Grade A")
elif marks <=69 and marks >=50:
    print("Grade B")
elif marks <=49 and marks >=35:
    print("Grade C")
else:
    print("Fail")
