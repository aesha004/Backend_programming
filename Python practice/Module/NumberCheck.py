def checkEvenOdd(num):
    if num % 2 == 0:
        return "Number is Even "
    else:
        return "Number is Odd "
    

def checkPosNeg(num):
    if num > 0:
        print("Number is Positive ")
    else:
        print("Number is Negative ")
    

def checkPrime(num):
    if num < 2 :
        return "Number is Not Prime"
    for i in range(2,num):
        if num % i == 0:
            return "Number is Not Prime"
    else:
        return "Number is Prime "
    

