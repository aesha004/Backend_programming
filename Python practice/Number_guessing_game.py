# Number Guessing game without hint for users
"""import random
number = random.randint(1,10) #random number selected by compiler
while True: # while loop because we dont know actual no of iterations 
    guess_number = int(input("Enter a number:  ")) # number guess by user
    if guess_number == number:                      # check if compiler number is same as user guessed number
        print("Congratulations you have guessed correct number !! ")
        break
"""

# With Hint for users
import random
number = random.randint(1,50)
while True:
    guess_number = int(input("Enter a number:  "))
    if guess_number > number:
        print("Number is too high")
    elif guess_number < number:
        print("Number is too low")
    else:
        print("Congratulations you have guessed correct number !! ")
        break