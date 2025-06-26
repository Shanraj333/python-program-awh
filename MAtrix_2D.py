size=int(input("Enter the size:"))
print("Enter first matrix:")
A = []
for i in range(size):
    row = list(map(int, input().split()))
    A.append(row)
print("Enter second matrix:")
B = []
for i in range(size):
    row = list(map(int, input().split()))
    B.append(row)
def add(A,B):
    C = []
    for i in range(size):
        row = []
        for j in range(size):
            row.append(A[i][j] + B[i][j])
        C.append(row)

    return C
def sub(A,B):
    C=[]
    for i in range(size):
         row=[]
         for j in range(size):
             row.append(A[i][j] - B[i][j])
         C.append(row)
    return C


def mul(A,B):
    C=[]
    for i in range(size):
         row=[]
         for j in range(size):
              row.append(A[i][j] + B[i][j])
         C.append(row)
    return C
print("Enter the choice:\n"
      "1.Addition\n"
      "2.Subtraction\n"
      "3.Multiplication\n")
ch=int(input())
if ch==1:
    k=add(A,B)
    for row in k:
       print(row)
elif ch==2:
    k=sub(A,B)
    for row in k:
       print(row)
elif ch==3:
    k=mul(A,B)
    for row in k:
       print(row)
else:
    print("Invalid!!\n")