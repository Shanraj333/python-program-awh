fruits = input("Enter the fruits separate it by commas:")
fruits=fruits.split(",")
dict_fruits = {}
for fruit in fruits:
    if fruit in dict_fruits:
            dict_fruits[fruit]+=1
    else:
        dict_fruits[fruit] = 1
print(dict_fruits)