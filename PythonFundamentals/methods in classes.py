class person:
    def __init__(self,fname,lname): #init is always first #self is used to access variables 
        self.fname = fname
        self.lname = lname
    def new(self): #Defining an extra function in the class
        #we give it self parameter to access the variables 
        print("Hi, my name is " + self.fname)
        print("Hi, my name is " + self.lname)

newPerson = person("Dony","adam")
print(newPerson.fname)
newPerson.new() #To call method put . To call init use = name of the class