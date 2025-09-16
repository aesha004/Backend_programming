# step - 1 to check no of digits
number = int(input("Enter a number: "))
count = 0
temp = number # temp to save copy of original number for last comparison
while(temp > 0):
    count+=1
    temp = temp // 10 # removes last digit to count the no of digits
    #print(temp)
print(f"Number of digits in entered number is : {count}")

# step - 2 amstrong number logic
temp = number
sum = 0
while(temp > 0):
    rem = temp % 10
    #print(f"{rem} = {temp} % 10")
    power = rem ** count
    print(f"{power} = {rem} ** {count}")
    sum += power
    print(f"{sum} = {sum} + {power}") 
    temp = temp // 10
    #print(temp)

# step - 3 comparison condition to compare originalnum = sum
if number == sum :
    print(f"Number is  {number} == {sum} is the sum of entered number")
    print(f"{number} is a amstrong number")
else : 
    print(f"{number} is not a amstrong number")

