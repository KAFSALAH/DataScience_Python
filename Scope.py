#scope 
x = 10
def new():
    global x
    x = 20
    print (x)
new() # calling what is inside the new function 
print(x) # global calling
#However, by using global command, we can call what is inside to the outside

