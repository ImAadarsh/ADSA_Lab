def allocate_lockers(num_jokers):
    lockers = list(range(1, num_jokers + 1))  # List of lockers
    allocate([], lockers)  # Start allocation process

def allocate(allocations, remaining_lockers):
    if len(allocations) == len(remaining_lockers):
        print(allocations)  # Print allocation when all lockers are allocated
        return
    
    for locker in remaining_lockers:
        if locker != len(allocations) + 1:  # Ensure no joker places stuff in designated place
            allocate(allocations + [locker], [l for l in remaining_lockers if l != locker])

if __name__ == "__main__":
    num_jokers = int(input("Enter the number of jokers: "))
    allocate_lockers(num_jokers)
