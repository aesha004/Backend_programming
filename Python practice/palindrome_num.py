num = int(input("Enter a number : "))
temp = num
reverse = 0
while (temp > 0):
    rem = temp % 10
    print(f"{rem} = {temp} % 10")
    temp = temp // 10
    print(f"{temp} = {temp} // 10")

    print(f"reverse: {(reverse * 10) + rem} = ({reverse} * 10) + {rem}")
    reverse = (reverse * 10) + rem

if reverse == num:
        print(f"{num} is a palindrome number")
else:
        print(f"{num} is not palindrome number")
