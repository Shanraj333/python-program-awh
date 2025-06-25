my_list = [5, 4, 7, 10, 8, 2]
index = int(input("Enter an index: "))

if 0 <= index < len(my_list):
    print(my_list[index:] + my_list[:index])
else:
    print("Index out of range")







