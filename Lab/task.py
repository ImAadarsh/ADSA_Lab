def find_power_set(numbers, target_sum):
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