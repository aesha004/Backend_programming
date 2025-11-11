# function declaration
def greet():
    print("Good Morning")

def close():
    print("Byeeee...")
    print("This is example of function")

greet() # function calling
greet()
close()


# Parameterised function
def greet(name,grade,age):
    print(f"Good Morning {name} your grade is {grade} and age is {age}")

greet("Aesha","A++",21)
greet("Heer","A",16)

# using same function take input from user for 3 students
"""for i in range(3):
    n = input(f"Enter {i+1} student name : ")
    g = input("Enter grade : ")
    a = input("Enter age : ")
    greet(n,g,a)"""

# Create a parameterized function that takes two arguments and prints their sum
def add(a, b):
    return a + b
result = add(5, 3)
print("Sum:", result)

# Create a function that takes a string as input and prints it. 
def display_message(text):
    print("You entered:", text)
user_input = input("Enter a string: ")
display_message(user_input)

# Calculator using functions
def add(a, b):
    return a + b
def subtract(a, b):
    return a - b
def multiply(a, b):
    return a * b
def divide(a, b):
    if b != 0:
        return a / b
    else:
        return "Cannot divide by zero"
print("Simple Calculator")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")

choice = input("Enter your choice (1/2/3/4): ")

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

if choice == '1':
    print("Result:", add(num1, num2))
elif choice == '2':
    print("Result:", subtract(num1, num2))
elif choice == '3':
    print("Result:", multiply(num1, num2))
elif choice == '4':
    print("Result:", divide(num1, num2))
else:
    print("Invalid Choice")
