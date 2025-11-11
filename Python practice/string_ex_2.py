""" Assignments tasks """
string = "Hello"
print(string)

str = '''Python Technology '''
print(str)
print(f"Printing first character of string : {str[0]}")
print(f"Printing string from second position onwards : {str[1:]}")
print(f"Printing a string upto fifth character : {str[0:5]}")
print(f"Printing substring between index 1 and 4 : {str[1:4]}")
print(f"Printing a string from last character : {str[::-1]}")
print(f"Printing every alternate character from the string starting from index 1 : {str[1::2]}  ")


# Write a Python program to find the length of each string in List1.
List1 = ["apple" , "banana" , "mango"]
for fruits in List1:
    print(f"{fruits} length =  {len(fruits)} ")

List1 = ['apple','Orange' , 'banana', 'mango']
for item in List1:
    if item == 'banana':
        print("Banana Found ! breaks the loop")
        break
    print(item)


# Write a Python program to find a specific string in the list using a simple for loop and if condition.
list = ["Kashmir" , "Kerela" , "Daman" , "Mumbai"]
search = input("Enter a string from list to search ")
found = False
for places in list:
    if places == search:
        print(f"{search} found in the list ")
        found = True
        break
else:
    print(f"{search} not found in the list ")
    

str1 = "Tops"
str2 = "12345"
str3 = "Tops@123"
str4 = "Tops tech"
print(f"{str1} str1.isdidgit() : {str1.isdigit()} , str1.isalpha() : {str1.isalpha()} , str1.isalnum() : {str1.isalnum()}")
print()
print(f"{str2} str2.isdidgit() : {str2.isdigit()} , str2.isalpha() : {str2.isalpha()} , str2.isalnum() : {str2.isalnum()}")
print()
print(f"{str3} str3.isdidgit() : {str3.isdigit()} , str3.isalpha() : {str3.isalpha()} , str3.isalnum() : {str3.isalnum()}")
print()
print(f"{str4} str4.isdidgit() : {str4.isdigit()} , str4.isalpha() : {str4.isalpha()} , str4.isalnum() : {str4.isalnum()}")



