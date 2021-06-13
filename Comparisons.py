#Comparison operators are, ==,!=,<=,>=, <,>.
#logic operators are and, or , not.
x = 4
y = 3
q = x > 3 and x>=y #"And" logic operator,  comparison "">" operator
s = not (x<2 or x !=4) #Not is used to reverese the condition
#print(s)
#-- 
#Identity operators are "is" and "not"
list1 = ["Fig", "apple"]
list2 = ["Fig", "apple"]
print(list1 == list2) #true
print(list1 is list2) #false
print(list1 is not list2) #true
#Membership operators "in"
print("fig" in list1) # false
print("Fig" in list1) # True
print("fig" not in list1) # false
