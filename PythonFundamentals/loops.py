#There are two loops in python, while and for.
#x = 1
#while x<7:
#    print(x)
#    if x ==3:
#        break #To break the looping
#    x += 1 # the same as x = x+1    
#print("end") # 

##Trying continue function
y = 1
while y <7:
    print(y)
    y +=1
    if y ==3:
        continue # To skip one iteration and go for the next one
    print("yes") 
#Udemy example for continue
x = 1
while x<7:
    x = x+1
    if x ==3:
        continue
    print(x)
else: 
    print ("The else statement at the end can be used with continue not break")