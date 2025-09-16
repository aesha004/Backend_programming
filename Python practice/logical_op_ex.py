number1 = int(input("Enter first number: "))
number2 = int(input("Enter second number: "))
ans = number1>100 and number1>number2
print(f"Answer of AND operator is: {ans}")

ans = number1>100 or number1>number2
print(f"Answer of OR operator is: {ans}")

ans = not(number1>100) # not (false because number1 is not greater than 100) = true
print(f"Answer of NOT operator is: {ans}")