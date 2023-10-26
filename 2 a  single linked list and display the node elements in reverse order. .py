class Node:
    def __init__(self, dataval=None):
        self.dataval = dataval
        self.nextval = None
class SLinkedList:
    def __init__(self):
        self.headval = None
    def listprint(self):
        printval = self.headval
        print("your List is :")
        while printval is not None:
            print (printval.dataval, end=' ')
            printval = printval.nextval
            print(end='\n')
    def reverse(self):
        prev = None
        current = self.headval
        while(current is not None):
            next = current.nextval
            current.nextval = prev
            prev = current
            current = next
            self.headval = prev
            list1 = SLinkedList()
            flag=1
        while flag==1:
            if list1.headval==None:
                data=int(input("Enter element"))
                n=Node(data)
                list1.headval=n
                temp=list1.headval
            else:
                data=int(input("Enter element"))
                n=Node(data)
                temp.nextval=n
                temp=n
                flag=int(input("do you want to continue(1/0)"))
            if flag==0:
                break
print("Your List is ",end='\n')
list1.listprint()
list1.reverse()
print("List after reverse",end='\n')
list1.listprint
