def find_subsets_with_sum(numbers, target_sum):
    subsets = []
    def backtrack(start, target, current_subset):
        if target == 0:
            subsets.append(tuple(current_subset))
            return
        for i in range(start, len(numbers)):
            if target - numbers[i] >= 0:
                backtrack(i + 1, target - numbers[i], current_subset + [numbers[i]])

    backtrack(0, target_sum, [])
    return subsets

# Example list of numbers
numbers = list(map(int, input("Enter the array elements (space-separated): ").split()))

# Get user input for the target sum
target_sum = int(input("Enter the target sum: "))


# Find and print subsets with the target sum
result_subsets = find_subsets_with_sum(numbers, target_sum)

if result_subsets:
    print(f"Subsets with sum equal to {target_sum}:")
    for subset in result_subsets:
        print(subset)
else:
    print(f"No subsets found with sum equal to {target_sum}.")
