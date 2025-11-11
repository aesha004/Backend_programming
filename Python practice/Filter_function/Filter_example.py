# filter even numbers from list of numbers 
def even(num):
    if num % 2 == 0:
        return "Even"
    
lst_numbers = [1,2,3,4,5,6]
lst_even = list(filter(even,lst_numbers))  
print("List of Even Numbers : ",lst_even)


