def insert_element(arr, element, position):
    new_array = []
    for i in range(len(arr) + 1):
        if i < position:
            new_array.append(arr[i])
        elif i == position:
            new_array.append(element)
        else:
            new_array.append(arr[i - 1])
    return new_array

def delete_element(arr, element):
    new_array = []
    element_found = False
    for value in arr:
        if value == element and not element_found:
            element_found = True
        else:
            new_array.append(value)
    if not element_found:
        print(f"{element} not found in the array.")
    return new_array


def linear_search(arr, key):
    for index, value in enumerate(arr):
        if value == key:
            return index
    return -1

def binary_search(arr, key):
    low, high = 0, len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == key:
            return mid
        elif arr[mid] < key:
            low = mid + 1
        else:
            high = mid - 1

    return -1

def bubble_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

# Example usage:
my_array = [5, 2, 9, 1, 3, 6, 12, 43, 124, 54]

# Insertion
my_array = insert_element(my_array, 8, 2)
print("Array after insertion:", my_array)

# Deletion
my_array = delete_element(my_array, 9)
print("Array after deletion:", my_array)

# Linear Search
search_key = 12
result = linear_search(my_array, search_key)
print(f"Linear search: {search_key} found at index {result}" if result != -1 else f"{search_key} not found")

# Binary Search (Note: Array must be sorted)
sorted_array = bubble_sort(my_array.copy())
search_key = 1
result = binary_search(sorted_array, search_key)
print(f"Binary search: {search_key} found at index {result}" if result != -1 else f"{search_key} not found")

# Bubble Sort
sorted_array = bubble_sort(my_array.copy())
print("Array after bubble sort:", sorted_array)

#