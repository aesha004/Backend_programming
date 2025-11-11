# check vowels and consonants present in string and if present then how many 
str = input("Enter a string : ")
vowels = 0
consonants = 0
for i in str:
    print(i)

for i in range(len(str)):
    if str[i] == 'a' or str[i] == 'e' or str[i] =='i' or str[i]=='o' or str[i]=='u'or str[i] == 'A' or str[i] == 'E' or str[i] =='I' or str[i]=='O' or str[i]=='U':
        print("Vowel present in entered string is : ",str[i]) 
        vowels +=1
    else:
        print("Not a vowel : ",str[i])
        consonants +=1

print(f"Total vowels are : {vowels}")
print(f"Not a vowel means Consonants are : {consonants}")


# Endswith function 
"""msg = "Hava a good day !!!"
print(msg.endswith("day"))
print(msg.endswith("good"))
print(msg.endswith("!!!"))
email = input("Enter your email : ")
if email.endswith(".com"):
    print(f"{email} is valid email address ")
else:
    print(f"{email} is not valid email address ")"""

# Accessing strings using loops
"""name = input("Enter a name: ")
for i in name:
    print(i)
# accessing with index also
for i in range(len(name)):
    print(f"{i} --> {name[i]}")"""