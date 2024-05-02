def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    
    # Taking first element as the pivot
    pivot = arr[0]  
    less_than_pivot = []
    equal_to_pivot = []
    greater_than_pivot = []

    for num in arr:
        if num < pivot:
            less_than_pivot.append(num)
        elif num == pivot:
            equal_to_pivot.append(num)
        else:
            greater_than_pivot.append(num)

    return quick_sort(less_than_pivot) + equal_to_pivot + quick_sort(greater_than_pivot)

# Driver code to run the quick_sort
unsorted_array = [3, 6, 8, 10, 1, 2, 1]
sorted_array = quick_sort(unsorted_array)

print("Unsorted Array:", unsorted_array)
print("Sorted Array:", sorted_array)