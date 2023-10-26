def main():
    arr = [12,2,5,67,43,56,2,1] 

    while True:
        print("\n1. Add Element to Array")
        print("2. Search Element in Array")
        print("3. Sort Array")
        print("4. Reverse Array")
        print("5. Display Array")
        print("6. Exit")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            element = int(input("Enter the element to add: "))
            arr.append(element)
            print("Element added to the array.")

        elif choice == 2:
            element = int(input("Enter the element to search: "))
            if element in arr:
                print(f"Element {element} found in the array at index {arr.index(element)}.")
            else:
                print(f"Element {element} not found in the array.")

        elif choice == 3:
            arr.sort()
            print("Array sorted in ascending order.")

        elif choice == 4:
            arr.reverse()
            print("Array reversed.")

        elif choice == 5:
            print("Array:", arr)

        elif choice == 6:
            print("Exiting the program.")
            break else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()
    
