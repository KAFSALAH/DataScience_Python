# For loop is used to iterate over a tuple, list, etc. Used with strings.
# fruits = ["banana","apple","fig"]
# for item in fruits: #Item represents each item 
#     print(item)

drink="Bananamilkshake"
for z in drink:
#To illustrate a break in for, observe below,
    if z == "m":
        continue
    print(z)
