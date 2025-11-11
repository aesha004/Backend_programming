# Aesha ---> shaAe 
# Hitesh ---> eshHit
name=input("Enter name ")
str_len = len(name)
print(f"Length of string : {str_len}")
half_len = str_len // 2
print(half_len)
first_part = name[:half_len]
print(f"First part of string : {first_part}")
second_part = name[half_len:]
print(f"Second part of string : {second_part}")
final = second_part + first_part
print(f"Final string is : {final}")


# Aesha ---> aeshA
name = input("Enter a name: ")
swapped =  name[-1] + name[1:-1] + name[0]
print(f"String after swapping is :{swapped}")


# Slicing with positive index [start:end:step]
name = "Tops Technologies"
print(name[0:5]) #Tops
print(name[4:10]) # Techn
print(f"upto 10 letters :{name[:10]}") #Tops Techn
print(f"from 5th letter to end :{name[5:]}") #Technologies
print(f"Printing alternate letters from whole string:{name[::2]}") #Tp ehoois
print(f"from 5th letter to end with alternate letter :{name[5::2]} ") #Tcnlge

# Slicing with negative index
"""name1 = "Placement Institute"
print(f" Last letter of string  as negative index start from -1 :{name1[-1]}") #e
print(f" Want last 10 letters from string :{name1[-10:]}") # Institute
print(f" Want 1st first 5 letters from string :{name1[-19:-14]}") #Place
print(f" Start of string to end with alternate using negative index :{name1[-19:-1:2]}") #PaeetIsiu
print(f" printing whole string using negative index :{name1[-19::]}") #Placement Institute
print(f" Reversed whole string :{name1[::-1]} ") #etutitsnI tnemecalP
print(f"-14th index to end of string :{name1[-14::]}") #ment Institute
print(f"from between to string -14th to -6th :{name1[-14:-6]}") #ment Ins """