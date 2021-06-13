#Dict nowadays are mutable, ordered. 
person = {
"name" : "Fred",
"Age" : 30,
"Country" : "Germany",
}
#print(person)
#len(person) to find length 
a = person ["name"]
b = person ["Age"]
c = person ["Country"]
#The other way to take info from dict is by using .get as below
#print(person.get("Age"))
#To know which keys are in the dict, use .keys(), for values type .values()
#print(person.keys())
#print(person.values())
#To present the dict in tuples, use. items
#print(person.items())
#to check if in item in the dict
#if "nae" in person:
#    print("yes")
#else:
#    print("no")
##To update, or add values of a key do this,
person ["Age"] = 45
##TO update or add, we could use update also, here update and adding simultaneously 
person.update({"Age":10, "ID" :432})
person.pop("Age") #Use popitem() to remove last item
#del person ["age"] to completely delete it, or person.clear()
print (person.items())