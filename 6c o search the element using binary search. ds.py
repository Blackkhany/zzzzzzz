def linearSearch(array, n, x):
    for i in range(0, n):
        if array[i] == x:
            return i
    return -1

array = []
size = int(input("Enter the size: "))
for i in range(size):
    abc = int(input("Enter the element: "))
    array.append(abc)

print("Array is: ", array)

x = int(input("\nEnter the element to be searched: "))
n = len(array)
result = linearSearch(array, n, x)

if result == -1:
    print("Element not found")
else:
    print("Element found at index: ", result)
