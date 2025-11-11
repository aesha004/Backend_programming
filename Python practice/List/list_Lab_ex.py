#  Convert names into upper case from list 
lst_name = ['Aesha' , 'Heer' , 'Meera' , 'Pinky']
print(lst_name)
for i in lst_name:
    name = i .upper()
    print(f"Names of list in upper case : {name}" )

#  Find length of each string from list
lst_name = ['Aesha' , 'Heer' , 'Meera' , 'Pinky']
print(lst_name)
for i in lst_name:
    length = len(i)
    print(f"length of {i} is : {length} ")

# Part -1 Find largest string from list using loop
lst_names = ['Aesha' , 'Heer' , 'Meera' , 'Pinky', 'Hitesh']
print(lst_names)
largest = lst_names[0] # assume first as largest to compare it with others
for words in lst_names:
    if len(words) > len(largest):
        largest = words  
print(f"Largest string by length is : {largest}")

# Part -2 Using max in-built function
lst_names = ['Aesha' , 'Heer' , 'Meera' , 'Pinky', 'Hitesh']
print(lst_names)
largest = max(lst_names,key = len)
print(f"Largest string by length is : {largest}")

# create valid email id list from exsting list e.g lst=['test@gmail.com','test.com','qwett@gmail.com','fdgdfggmail.com']
    # output --- valid_email_lst = ['test@gmail.com','qwett@gmail.com']
lst=['test@gmail.com','test.com','qwett@gmail.com','fdgdfggmail.com']
print(lst)
gmail_lst = []
for email in lst:
    if email.endswith("@gmail.com"):
        gmail_lst.append(email)
print(f"Filtered email list : {gmail_lst}")

# Part -1  Find second higest number from lst=[11,23,32,9,23] using sort and index inbuilt functions
lst_number = [11,23,32,9,23]
lst_number.sort(reverse = True)
print(f"Sorted list numbers : {lst_number}")
print(f"Second Higest number in list is : {lst_number[1]}")

# Part - 2 same using logic if-else
lst_number = [12, 45, 67, 23, 89, 34]
largest = second_largest = lst_number[0]
for i in lst_number:
    if i > largest:
        second_largest = largest
        largest = i
    elif i > second_largest and i != largest:
        second_largest = i
print(f"Second Higest number in list is : {second_largest}")


# find no of vowels in string from list input ['test','testa','tst'] output [1,2,0]
lst_name = ['Aesha' , 'Heer' , 'Aarya' , 'tst']
print(lst_name)
new_list  = []
for string in lst_name:
    print(string)
    vowels = 0 # reset vowels for each string
    for i in range(len(string)):
        if string[i] in 'AEIOUaeiou':
            vowels += 1
    new_list.append(vowels)
print(f"Total vowels in each string in new list : {new_list}")