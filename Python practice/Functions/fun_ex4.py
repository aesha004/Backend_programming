# using **kwargs with Regular Arguments
def my_fun (username , **details):
    print("Username : ",username)
    print("Additional Details : ")
    for key,value in details.items():
        print(" ", key + ":" , value)
my_fun("Aesha123" , age = 25 ,city = "Khambhat" , hobby ="coding")

# fix parameter name and other details may be differ 