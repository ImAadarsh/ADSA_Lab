def binary_search(arr, target):
    low, high = 0, len(arr) - 1
    
    while low <= high:
        mid = (low + high) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return -1  # Element not found

# User input for the array
arr = list(map(int, input("Enter the array elements (space-separated): ").split()))

# User input for the element to search
target = int(input("Enter the element to search: "))

# Perform Binary search
index = binary_search(arr, target)

# Display the result
if index != -1:
    print(f"The element {target} is found at index {index}.")
else:
    print(f"The element {target} is not present in the array.")

