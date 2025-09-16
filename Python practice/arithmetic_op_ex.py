num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
# Format function (1st way) used to print the addition of two numbers
print("Addition of {} and {} is {}\n" .format(num1 , num2 , num1+num2))

# F string (2nd way) used to print the subtraction of two numbers
print(f"Subtraction of {num1} and {num2} is {num1-num2}\n")
print(f"Multiplication of {num1} and {num2} is {num1*num2}\n")
# Division gives float value
print(f"Division of {num1} and {num2} is {num1/num2}\n")
# Modulus gives remainder value
print(f"Modulus of {num1} and {num2} is {num1%num2}\n")
# While Floor division gives integer value
print(f"Floor Division of {num1} and {num2} is {num1//num2}\n")
# Exponentiation gives power value
print(f"Exponentiation of {num1} and {num2} is {num1**num2}\n")

#lab task 
str = input("Enter a string: ")
num = int(input("Enter a number: "))
print("Exponent is:",str**num)