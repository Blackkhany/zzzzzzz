import sys

S = list()
S.append(5)
S.append(7)
S.append(3)
S.append(1)
S.append(5)
S.append(7)

print("Stack is:")
print(S)

top = None

def isEmpty(stk):
    if not stk:
        return True
    else:
        return False

def push(stk, item):
    stk.append(item)
    top = len(stk) - 1

def pop(stk):
    if isEmpty(stk):
        return 'UNDERFLOW'
    else:
        i = stk.pop()
        if len(stk) == 0:
            top = None
        else:
            top = len(stk) - 1
        return i

def display(stk):
    if isEmpty(stk):
        print('Stack is empty!')
    else:
        print("Stack is:", stk)

def menu():
    print("Menu:")
    print("1. PUSH")
    print("2. POP")
    print("3. DISPLAY")
    print("4. EXIT")
    return int(input("Enter your choice: "))

while True:
    choice = menu()
    if choice == 1:
        item = int(input("Enter element to be added: "))
        push(S, item)
        print('%d added successfully' % item)
        print("New Stack is:")
        print(S)
        print()
    elif choice == 2:
        item = pop(S)
        if item == 'UNDERFLOW':
            print('UNDERFLOW! Stack is Empty!')
        else:
            print('%d is popped' % item)
        print("New Stack is:")
        print(S)
        print()
    elif choice == 3:
        display(S)
    elif choice == 4:
        print("Exiting............")
        sys.exit()
