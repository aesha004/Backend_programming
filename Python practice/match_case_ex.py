print ("\n  1. Addititon \n  2. Subtraction \n  3. Multiplication \n  4. Division \n  5. Floor Division \n  6. Exponent ")
num1 =int(input("Enter 1st number: "))
num2 =int(input("Enter 2nd number: "))
choice = input("Enter your Choice in signs : ")
match choice:
    case '+':
        print(f"Addition of {num1} and {num2} is : {num1 + num2}")
    case '-':
        print(f"Subtraction of {num1} and {num2} is : {num1 - num2}")
    case '*':
        print(f"Multiplication of {num1} and {num2} is : {num1 * num2}")
    case '/':
        print(f"Division of {num1} and {num2} is : {num1 / num2}")
    case '//':
        print(f"Floor Division of {num1} and {num2} is : {num1 // num2}")
    case '**':
        print(f"Exponent of {num1} and {num2} is : {num1 ** num2}")
    case _:
        print("Invalid Choice ")