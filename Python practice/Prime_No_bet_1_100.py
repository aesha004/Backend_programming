# Using For Loop
print("Prime Numbers Between 1 - 100 is :  ")
 # temporaray variable to check prime number is divisible or not
for i in range(2, 100):    # Start from 2 t0 100, since 1 is not prime
    temp = 0           # temp used here to reset value of temp after incrementing value of i
    for j in range(2, i):  # j will Check divisors from 2 up to i-1 for every value of i
        if i % j == 0:     # if divisible
            temp = 1       # then marks as "not prime"
            #print(f"i = {i} j = {j}")
            break             # stop checking  
        else:                       
            temp = 0   # If it finds not divisible → the else runs, printing the "prime".
    if temp == 0:
        print(i,end = " ")



# using While Loop
print("Prime Numbers Between 1 - 100 is :  ")
temp = 0
i = 2
while i<=100:
    j = 2
    while j<i:
        if i % j == 0:
            temp = 1
            break
        else:
            temp = 0
        j+=1
    if temp == 0:
        print(i,end=" ")
    i+=1
