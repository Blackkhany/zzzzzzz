def main():
    arr1 = []
    arr2 = []

    while True:
        print("\n1. Read Array 1")
        print("2. Read Array 2")
        print("3. Merge and Sort Arrays")
        print("4. Display Merged and Sorted Array")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            arr1 = read_array()
            print("Array 1 read successfully.")

        elif choice == "2":
            arr2 = read_array()
            print("Array 2 read successfully.")

        elif choice == "3":
            merged_array = sorted(arr1 + arr2)
            print("Arrays merged and sorted successfully.")

        elif choice == "4":
            if 'merged_array' in locals():
                print("Merged and Sorted Array:", merged_array)
            else:
                print("Please merge and sort the arrays first.")

        elif choice == "5":
            print("Exiting the program.")
            break

        else:
            print("Invalid choice. Please select a valid option.")

def read_array():
    arr = input("Enter space-separated elements of the array: ")
    arr = list(map(int, arr.split()))
    return arr

if __name__ == "__main__":
    main()
