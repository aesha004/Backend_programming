# Types of Function Arguments
# 1. Default Arguments 
def greet(name,age=20): # age=20 is default parameter where age value is not mention in function call it will take 20. 
    print("Good Morning ",name,age)
greet("Aesha",30)
greet("Heer")
greet("Prita")
greet("Aarya",22)

# 2. Keyword Arguments
def greet(name,msg):
    print(name,msg)
greet("Good morning","Aesha")
greet(msg="Good morning",name="Aarya")

# 3. Variable Arguments
# a. *args
def personDetails(*args):
    for i in args:
        print(i)

print("Person1 ")
personDetails(101,"Aesha",30)
print("Person2 ")
personDetails(201,"Aarya","BTech","Ahemedabad")
print("Person 3 ")
personDetails("Aisha","BTech","aisha@gmail.com",1213134)
    

def my_fun (*kids):
    print("Type :",type(kids))
    print("The Youngest kid is : " + kids[3])
my_fun("Dev","Shrivi","Shivang","Kiaan")


def addition(*args):
    sum = 0
    for i in args:
        if type(i) == int:
            sum += i
        return sum
print(addition(12,23))
print(addition(20,"aesha",80))
print(addition(50,50,"abc"))

# b. **kwargs  
def personDetails(**kwargs):
    print(kwargs)
# def details():
#     return 1,"Dharmishtha",30,"Python"
personDetails(name="Aesha",age=30)
personDetails(city="Ahedmbad",name="Aarya",age=20)
personDetails(name="Aisha",age=22)
personDetails(name="Prita",age=30)
# print(details())


def personDetails(**kwargs):
    if kwargs['age']>=30:
        print(kwargs['name'])
personDetails(name="Aesha",age=30)
personDetails(city="Ahedmbad",name="Aarya",age=20)
personDetails(name="Aisha",age=22)
personDetails(name="Prita",age=30)
