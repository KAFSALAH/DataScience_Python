#Python is object-oriented programming language 
#We put functions inside classes, and call classes to call functions
#In that way, we can call functions as many times as we want without interfering between valeus 
class person:
    """Create a new person """
    #A variable inside a class is called an attribute 
    #We are going to define a function to assign values to objects in the class
    #all classes have function called init, always executed in the initiating of a class
    def __init__(self,fname,lname):
        self.fname = fname
        self.lname = lname
#self parameter is a reference to the instance of the class
#used to acess the variables insdie the class 
newPerson = person("Dony", "Steve") #Classes inserts our input directly to the functions 
secondNewPerson = person("Johny","Saleh")
#Displaying the output
print(newPerson)
print(newPerson.fname)
print(newPerson.lname)
# print(secondNewPerson)
# print(secondNewPerson.fname)
# print(secondNewPerson.lname)
newPerson.fname = "adam"
print(newPerson)
print(newPerson.fname)
print(newPerson.lname)

#del to delete a property to assigned to an object
# del can delete the whole object also 
## Methods are functions inside a class