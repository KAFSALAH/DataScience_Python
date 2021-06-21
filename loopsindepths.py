#Repeting as the number of elements 
#The i is a loop adjusted by number of elements
squares = ["Red","yellow","green","purple","blue"]
for i in squares:
    print(squares)
#Changing the elements in a specific range:
#the range here is from index 0 to 4 
for i in range(0,5):
    squares[i] = 'white'
    #If we put print here, it would have been printed five times
print(squares)
#Another Example would be as follows,
for x in range(0,3):
     print(x)
#Also,
for x in ['A','B','C']:
  print(x+'A')
#enumerate is powerful tool to get the index with the element
for (i,x) in enumerate(['A','B','C']):
    print(i,x)
#For is used to perfom for a certain number of times,
#While is uded to perform while a condition is met
squares2 = ['orange','oragne','orange','purple','black', 'orange']
newsquares=[]
i = 0
while(squares2[i]=='orange'):
    newsquares.append(squares2[i])
    i=i+1
print(newsquares)
# For loop Extra example
dates = [1982,1980,1973]
N = len(dates)
for i in range(N):
    print(dates[i])    