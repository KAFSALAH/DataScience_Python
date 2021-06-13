# lists are [] mutables, ordered, and allow duplicate
s = [4,0,10]
# tuples are () Immutables, ordered, and allow duplicate 
v = (2,7)
# sets are {} are immutables, unordered, and does not allow duplicate 
q = {2,8}
# Dictionary
newDict = { "key1": "value1", "key2": "value2"}
# To change an element in the list, use this
#s[0]= 1
# To chane complete portion in lists, use this, and notice the tricky
# of the increment of 1 
#index 2 is not included 
s[0:2] = [5,7]
print(s)
# To insert an element, use this 
s.insert(1,"Yes I inserted it successfuly")
s.insert(2,"Yes")
print(s[4])
