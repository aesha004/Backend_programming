while True:
    count = 0
    print(" \n1. Reverse a Number  \n2. Find no of digits  \n3. Count total even and odd digits from a number   \n4. Check number is palindrome  \n5. Exit ")
    choice = int(input("Please enter your choice : "))
    match choice:
        case 1:
            num=int(input("Enter a number to be reversed : "))
            int_str_no = str(num)
            print(f"Reversed number is {int_str_no[::-1]}")
        
        case 2:
            num = int(input("Enter a number to find no of digits in it : "))
            while num!= 0:
                remainder = num % 10
                num = num // 10
                count += 1
            print(f"No of digits present in a number is : {count}")
        
        case 3:
            even = 0
            odd  = 0
            num = int(input("Enter a number to find no of even and odd digits in it : "))
            while num!=0:
                remainder = num % 10
                if remainder %  2 == 0:
                    even += 1
                else:
                    odd +=1
                num = num // 10
            print(f"Total no of even digits is : {even}")
            print(f"Total no of odd digits is : {odd}")
        
        case 4:
            num = int(input("Enter a number to check it is palindrome or not : "))
            temp = num
            reverse = 0
            while (temp > 0):
                remainder = temp % 10
                temp = temp // 10
                reverse = (reverse * 10) + remainder
            
            if reverse == num:
                print(f"{num} is a palindrome number")
            else:
                print(f"{num} is not a palindrome number")
            
        case 5:
            break
        
        case _:
            print("Enter valid choice ")
