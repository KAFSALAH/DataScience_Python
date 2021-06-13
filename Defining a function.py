#Defining a function 
def addNumbers(a,b):
    result = a+b
    return result
print(addNumbers(4,5))
#Use many return 
def basicMath(x,y):
    sum = x+y
    mult=x*y
    divide= x//y
    return sum, mult, divide
print("the values are", basicMath(10,3))
#Anonymous lambda
x = lambda i,t: i*t
print(x(2,3))
#Calling a function 
def new():
    y = int(input("please enter a number"))
    x = int(input("please enter a number"))
    print (x+y)
new()
def name():
    x = str(input("PLease enter you fname\n"))
    y = str(input("Please enter you lname\n"))
    print("your name is", x,y)
name()