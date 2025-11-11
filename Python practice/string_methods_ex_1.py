c_name = "Aesha Patel Patel"
s=c_name.find("e")
print(s)
print(c_name.find("e",4,10)) # "Find" function (substring,start,end) 
print(c_name.find("y")) # in find if substring not found then it will return -1 index

print("Count Occurrences of e :",c_name.count("e")) # "Count" function will count the occurrences of substring
print(c_name.count("a P"))
print(c_name.count("Patel"))

print("Length of string :",len(c_name)) # "Length" function will gives the length of whole string 

# Lab task
sentence = "cat is animal and dog is animal"
print("Occurrence of animal word is : ",sentence.count("animal"))


# # lab task - take 5 string from user and perform upper,lower,title,capitalize operations
# for i in range(1,5):
#     user_input = input(f"Enter a String {i} : ")

#     if i==1:
#         print("Lower Case : ",user_input.lower())
#         print()
#     elif i==2:
#         print("Upper Case : ",user_input.upper())
#         print()
#     elif i==3:
#         print("Title Case : ",user_input.title())
#         print()
#     elif i==4:
#         print("Capitalize : ",user_input.capitalize())
#         print()
#     else:
#         print("Original String : ",user_input)


c_name = "tops technologies"
s=c_name.upper()
print("Upper : ",s)

s=c_name.lower()
print("Lower : ",s)

s=c_name.capitalize()
print("Capitalize : ",s)

s=c_name.title()
print("Title : ",s)

name ="Aesha Patel"
print("Length of string : ",len(name))


s="Python is fun"
print(s.replace("fun","Awesome")) # "replace" function to replace old string with new string 
s="Python is so so easy"
print(s.replace("so","very",2)) # also count = 2 means replace 2 times "so" with "very" string

# replace function using user input
sentence = input("Enter a sentence: ")
print(f"Original sentence : {sentence}")
word = input("Enter a word to replace : ")
new_word = input("Enter a new word : ")
new_sentence = sentence.replace(word , new_word)
print(f"New Sentence is : {new_sentence}")


txt ="Hello,Welcome"
print(txt.index("e")) # gives whenever first "e" is found
print(txt.index("l",5,11)) # index(string,start,end) starts from 5th index till 11th index and search for "l" letter
#print(txt.index("q")) # error substring not found


