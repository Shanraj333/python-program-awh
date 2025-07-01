n=int(input("Enter the size of the list:"))
list=[int(input(f"Enter the number{i+1}:")) for i in range(n)]
print(list)
list.sort()
print(list)
print("the largest number is:",list[-1])
print("The second largest number is:",list[-2])
