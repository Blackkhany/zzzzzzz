def insertionSort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

arr = []
size = int(input("Enter the size of the element: "))
for i in range(size):
    x = int(input("Enter the element: "))
    arr.append(x)

print("Array before sorting: ", arr)
sorted_array = insertionSort(arr)
print("Sorted array is: ", sorted_array)
