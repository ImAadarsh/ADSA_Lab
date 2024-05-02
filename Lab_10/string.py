def brute_force_string_matching(text, pattern):
    n = len(text)
    m = len(pattern)

    for i in range(n - m + 1):
        j = 0
        while j < m and text[i + j] == pattern[j]:
            j += 1
        if j == m:
            return i  # pattern found at index i
    return -1  # pattern not found


# Example usage:

text = "ADARSH KUMAR GUPTA FROM NIT JALANDHAR"
pattern = "NIT"
index = brute_force_string_matching(text, pattern)

if index != -1:
    print(f"Pattern found at index {index}.")
else:
    print("Pattern not found.")
