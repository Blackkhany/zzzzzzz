import sys
row=int(input("Enter the row number for matrix1: "))
col=int(input("Enter the column number for matrix2: "))
row_col=int(input("Enter the column number for matrix1/row number of matrix2: "))
print("Enter the elements for matrix1: ")
matrix1=[[int(input())for i in range(col)] for j in range(row)]
print("matrix1:")
for i in range(row):
    for j in range(col):
        print(matrix1[i][j],end=" ")
    print()
print("Enter the elements for matrix2: ")
matrix2=[[int(input())for i in range(col)] for j in range(row)]
print("matrix2:")
for i in range(row):
    for j in range(col):
        print(matrix2[i][j],end=" ")
    print()
def menu():
    print("MENU IS:",end="\n")
    print("1. Addition",end="\n")
    print("2. Multiplication",end="\n")
    print("3. Transpose",end="\n")
    print("4. Exit",end="\n")
    choice=int(input("Enter your choice: "))
return choice
while True:
    row=col
    choice=menu()
    if choice==1:
        Addition=[[0 for i in range(col)] for j in range(row)]
print("Addition of matrix is: ")
for i in range(row):
    for j in range(col):
        Addition[i][j]=matrix1[i][j]+matrix2[i][j]
for i in range(row):
    for j in range(col):
        print(Addition[i][j],end=" ")
    print()
elif choice==2:
    multiplication=[[0 for i in range(col)] for j in range(row)]
    print("Multiplication of matrix is: ")
for i in range(row):
    for j in range(col):
        for k in range(row_col):
            multiplication[i][j]=multiplication[i][j]+matrix1[i][k]*matrix2[k][j]
for i in range(row):
    for j in range(col):
        print(multiplication[i][j],end=" ")
    print()
elif choice==3:
    transpose=[[0 for i in range(col)] for j in range(row)]
    print("Transpose of matrix1 is: ")
for i in range(row):
        for j in range(col):
            transpose[i][j]=matrix1[j][i]
    for i in range(row):
        for j in range(col):
            print(transpose[i][j],end=" ")
        print()
    transpose=[[0 for i in range(col)] for j in range(row)]
    print("Transpose of matrix2 is: ")
    for i in range(row):
        for j in range(col):
            transpose[i][j]=matrix2[j][i]
    for i in range(row):
        for j in range(col):
            print(transpose[i][j],end=" ")
        print()
elif choice==4:
    print("Exit")
    print()
    sys.exit()
