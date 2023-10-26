import sys
q=[]
while True:
    print("Menu is",end="\n")
    print("1. INSERT:",end="\n")
    print("2. DELETE:",end="\n")
    print("3. DISPLAY:",end="\n")
    print("4. EXIT:",end="\n")
choice=int(input("ENTER YOUR CHOICE: "))
if choice==1:
    a=int(input("Enter the number to insert: "))
    q.append(a)
    print(q)
elif choice==2:
    s=q.pop(0)
    print(q,"Element deleted",s)
elif choice==3:
print(q)
elif choice==4:
print("Exiting..............")
sys.exit()
menu()
