# Pattern - 1 *
#             * *
#             * * *
#             * * * *
"""num = int(input("Enter number "))
for i in range(num):
    for j in range(i):
        print("*",end=" ")
    print()"""

# pattern - 2 1
#             1 2
#             1 2 3
#             1 2 3 4
#             1 2 3 4 5
"""num = int(input("Enter number "))
for i in range(1,num+1):
    for j in range(1,i+1):
        print( j ,end=" ")
    print() """

# pattern - 3 1
#             2 2
#             3 3 3
#             4 4 4 4
#             5 5 5 5 5
num = int(input("Enter number "))
for i in range(1,num+1):
    for j in range(1,i+1):
        print( i ,end=" ")
    print()

# pattern - 4 * * * * *
#             * * * *
#             * * *
#             * *
#             *
num = int(input("Enter number "))
for i in range(num,0,-1):
    for j in range(0,i):
        print("*",end=" ")
    print()


