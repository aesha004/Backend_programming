# Split Function - Splits a string into list
name = "Tops technologies Pvt ltd"
lst = name.split()
print(lst)
# Splitting with a specific letter like t here
lst1 = name.split("t")
print(f" Split by t : {lst1}")

# Counting no of words from a Sentence
sentence = "Today is 3rd day of auspicious Navratri"
list = sentence.split()
print(f"Split sentence to find no of words : {list}")
no_of_word = len(list)
print(f"Total words present in sentence is : {no_of_word}")

# Join Function - Used to join elements of an (list , tuple , or set) into  single string
list3 = ['Apple', 'Cherry' , 'Guava' , 'Banana']
fruits =" ".join(list3)
print(f"Join list3 with space: {fruits}")
fruits ="**".join(list3)
print(f"Join list3 with ** : {fruits}")