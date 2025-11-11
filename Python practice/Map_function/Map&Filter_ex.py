# list_city in upper whose length is more than 5 using both filter and map function
list_city = ["Anand" , "Ahmedabad" , "Khambhat"]
def check_len(str):
    if len(str) > 5 :
        return str
lst_len = list(filter(check_len,list_city))
print("Cities having length greater than 5 : " ,lst_len) 

lst_upper = list(map(str.upper,lst_len))
print(f"String in Uppercase whose length is > 5 : {lst_upper}")

# square of even numbers in list using both filter and map function
lst_numbers =[1,2,4,6,7,9]
def check_even(num):
    if num % 2 == 0:
        return "Even"
    
def square(num):
    return num * num 

lst_even = list(filter(check_even,lst_numbers))
print(lst_even)

lst_ans = list(map(square,lst_even))
print("Square of even Numbers : ",lst_ans)