def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i  
    return -1  

# User input for the array
arr = list(map(int, input("Enter the array elements (space-separated): ").split()))

# User input for the element to search
target = int(input("Enter the element to search: "))

# Perform linear search
index = linear_search(arr, target)

# Display the result
if index != -1:
    print(f"The element {target} is found at index {index}.")
else:
    print(f"The element {target} is not present in the array.")
