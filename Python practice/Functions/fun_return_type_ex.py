# function with return type
# 1. Check Entered number is Even or Odd
"""def checkNumber(num):
    if num%2 == 0:
        return "Even"
    else:
        return "ODD"

ans = checkNumber(int(input("Enter a number : ")))
print(f"Number is {ans}")"""


# 2. From 1 t0 50 Check every number whether it is even or odd
"""for i in range(50):
    print(f"{i} --> {checkNumber(i)}")"""


# 3. Create function which accept a number and return "Prime" or "Not Prime"
"""def checkPrime(num):
    if num <= 1 :
        return "Not Prime"
    for i in range(2 , int(num ** 0.5) + 1):  # range from 2 to (square root of num) + 1 this gives divisors of number
        if num % i == 0:   # check number with each divisors if not found reminder
            return "Not Prime"
    else:                  # found reminder 
        return "Prime"
    
result = checkPrime(int(input("Enter a number: ")))
print(f"Number is {result}.")"""


# 4. Create function to check string is palidrome or not 
def checkPalindrome(string):
    new_str = string
    if new_str == string[::-1]:
        return "Palindrome"
    else:
        return "Not Palindrome"
    
result_string = checkPalindrome(input("Enter a string : "))
print(f"String is  {result_string}")

