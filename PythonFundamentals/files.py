# TO create a file use write
text1='Text1.txt'
with open(text1,'w') as writing: #Write everything from zero (i.e., Overwrite)
     writing.write("This is first line\n")
with open(text1,'r') as reading: #reads thevalues
   x= reading.read()
print(x)
with open(text1,'a') as writing: #aapending
     writing.write("This is second line\n")
with open(text1,'r') as reading:
   x= reading.read()
print(x)