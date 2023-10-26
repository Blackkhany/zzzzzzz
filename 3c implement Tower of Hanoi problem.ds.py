def hanoi(n, source, helper, target):
    print("hanoi(", n, source[1], helper[1], target[1], " called")

    if n > 0:
        # Move the tower of size n - 1 to the helper:
        hanoi(n - 1, source, target, helper)

        # Move the disk from the source peg to the target peg
        if source[0]:
            disk = source[0].pop()
            print("Moving " + str(disk) + " from " + source[1] + " to " + target[1])
            target[0].append(disk)

        # Move the tower of size n-1 from the helper to the target
        hanoi(n - 1, helper, source, target)

source = ([4, 3, 2, 1], "source")
target = ([], "target")
helper = ([], "helper")

hanoi(len(source[0]), source, helper, target)

print("Source:", source)
print("Helper:", helper)
print("Target:", target)
