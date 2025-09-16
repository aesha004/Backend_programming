number = int(input("Enter a number: "))
count = 0 # used to count total No. of digits at last
while number!=0 :  # first to check entered number is not 0
    rem = number % 10  # modulo to seperate each digit from whole number
    number = number // 10  # floor division to except number in "integer" only 
    count+=1
    print(f"Num = {number} Rem = {rem}") # for understanding purpose
print(f"No of digits in given number is : {count}")