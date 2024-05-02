def is_prime(num):
    if num < 2:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

# Get user input for the value of n
try:
    n = int(input("Enter the value of n: "))
except ValueError:
    print("Invalid input. Please enter an integer.")
    exit()

# Print prime numbers from 1 to n
print("Prime numbers from 1 to", n, "are:")
for number in range(2, n + 1):
    if is_prime(number):
        print(number)

