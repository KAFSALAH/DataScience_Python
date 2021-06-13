#We  use the function "open" which hast two parameters ("filename", "mood") to open files
#The moods are [r:read] [a:append] [w:write] [x:create]
#file = open ("empty.txt","r")
#print(file.read()) #Notice the paranthesis after read. #If we put numbers specifiy the length 
# print(file.readline()) #repeat read line to exess next lines 
# print(file.readline()) #repeat read line to exess next lines 
# print(file.readline()) #repeat read line to exess next lines 
#for x in file: # = print(file.read())
#print(x)
#after completing the task, close the file
#file.close
#To append content 
file = open ("empty.txt","a")
file.write ("\nAdd this to the text ")
file.close()
#To over write, or create new txt
file = open ("empty.txt","w")
file.write ("fgf")
file.close()
#also to create new, use x
#file = open ("eeeeepty.txt","x") # I deleted the file 
#file.write ("fgf")
#To delete via code, 
import os
os.remove("empty.txt")