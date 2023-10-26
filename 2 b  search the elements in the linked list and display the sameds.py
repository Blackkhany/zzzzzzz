class Node:
    def __init__(self, dataval=None):
        self.dataval = dataval
        self.nextval = None

class SLinkedList:
    def __init__(self):
        self.headval = None

    def listprint(self):
        printval = self.headval
        print("Your List is:")
        while printval is not None:
            print(printval.dataval, end=' ')
            printval = printval.nextval
        print()  # Just print a newline to separate the output.

    def search(self, ele):
        temp = self.headval
        found = 0  # It will change only if the element is found
        while temp is not None:
            if int(temp.dataval) == int(ele):
                print("Element is found")
                found = 1
                break
            temp = temp.nextval
        if found == 0:
            print("Element not found")

# Create an empty linked list
list1 = SLinkedList()
flag = 1

while flag == 1:
    if list1.headval is None:
        data = int(input("Enter element: "))
        n = Node(data)
        list1.headval = n
        temp = list1.headval
    else:
        data = int(input("Enter element: "))
        n = Node(data)
        temp.nextval = n
        temp = n
    flag = int(input("Do you want to continue (1/0): "))

print("Your List is:")
list1.listprint()
ele = int(input("Enter the element to be searched: "))
list1.search(ele)
 
