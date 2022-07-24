import ImportedM #importing other moduels from the library 
#import ImportedM as any # Help in giving it a nickname 
#ImportedM.yes("Salah") #Using the imported file (as like it is a class). the desired function 
#ImportedM.alpha() #As input
#x = ImportedM.player["name"]
#print(x)
#import platform # built-in 
#print(platform.system()) #To figure which system is being used 
#if we use dir, we can know all the functions in a moudle
#op = dir(platform)
#opp = dir(ImportedM)
#print(opp)
# import math
# print(math.cos(math.e))
#To import a singe entity use"from" as follows
from ImportedM import player 
x = player["name"]
print(x)
from math import cos
print(cos(2))