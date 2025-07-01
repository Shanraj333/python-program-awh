rows = int(input("Enter the number of rows:")) # Number of rows
for i in range(1,rows+1):
    print(" " * (rows-i), end="")
    print("* " * i)

