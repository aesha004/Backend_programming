# Strip Function - Removes all the leading and trailing spaces (spaces, tabs, newlines) from string 
name = " Tops Technologies "
print(f"Length with space included : {len(name)}")
name = name.strip()
print(f"After using strip function length is : {len(name)}")
name1 ="***Aesha***"
print(name1.strip("*")) # and if mention in function to remove particular special symbol. 

# Sorted Function - used to sort the elements of lists,tuples,set,strings and returns a new sorted list
name = "Aesha Patel"
print(sorted(name))

#Eg:- Want to sort words from a sentence
sentence = "Today is Wednesday!"
sen_split = sentence.split()
print(f"Splitted sentence : {sen_split} ")
sort_sen = sorted(sen_split)
print(f"Original sentence : {sentence} Sorted sentence : {sort_sen}")

sort_sen_len = sorted(sort_sen , key = len)  # key for parameters in which we want to sort a list or sentence 
print(f"Sorted sentence acc to length : {sort_sen_len}")
