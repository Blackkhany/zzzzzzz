def selectionSort(array):
    n = len(array)
    for i in range(n):
        minimum = i
        for j in range(i + 1, n):
            if array[j] < array[minimum]:
                minimum = j
        temp = array[i]
        array[i] = array[minimum]
        array[minimum] = temp
    return array

array = []
size = int(input("Enter the size of elements: "))
for i in range(size):
    x = int(input("Enter the element: "))
    array.append(x)

print("Array before sorting: ", array)
sorted_array = selectionSort(array)
print("Array after selection sorting: ", sorted_array)
