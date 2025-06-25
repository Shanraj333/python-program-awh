def add(a,b):
    c=a+b
    return c
def sub(a,b):
    c=a-b
    return c
def mul(a,b):
    c=a*b
    return c
def div(a,b):
    c=a/b
    return c
n = int(input("Enter a choice:"
              "1.Add"
              "2.Subtraction"
              "3.Multiplication"
              "4.division"
              "5.Exit"))

if n == 1:
    a=int(input("Enter a number:"))
    b = int(input("Enter another number:"))
    print(add(a,b))
elif n == 2:
    a=int(input("Enter a number:"))
    b = int(input("Enter another number:"))
    print(sub(a,b))
elif n == 3:
    a=int(input("Enter a number:"))
    b = int(input("Enter another number:"))
    print(mul(a,b))
elif n == 4:
    a=int(input("Enter a number:"))
    b = int(input("Enter another number:"))
    print(div(a,b))
else:
    print("Exit")