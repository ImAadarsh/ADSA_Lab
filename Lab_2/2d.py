def add_matrices(matrix1, matrix2):
    result = []
    for i in range(len(matrix1)):
        row = []
        for j in range(len(matrix1[0])):
            row.append(matrix1[i][j] + matrix2[i][j])
        result.append(row)
    return result

def subtract_matrices(matrix1, matrix2):
    result = []
    for i in range(len(matrix1)):
        row = []
        for j in range(len(matrix1[0])):
            row.append(matrix1[i][j] - matrix2[i][j])
        result.append(row)
    return result

def multiply_matrices(matrix1, matrix2):
    result = []
    for i in range(len(matrix1)):
        row = []
        for j in range(len(matrix2[0])):
            element = 0
            for k in range(len(matrix2)):
                element += matrix1[i][k] * matrix2[k][j]
            row.append(element)
        result.append(row)
    return result

def transpose_matrix(matrix):
    result = []
    for j in range(len(matrix[0])):
        row = []
        for i in range(len(matrix)):
            row.append(matrix[i][j])
        result.append(row)
    return result

# Example matrices
matrix_a = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

matrix_b = [
    [9, 8, 7],
    [6, 5, 4],
    [3, 2, 1]
]

# Matrix addition

  
result_addition = add_matrices(matrix_a, matrix_b)
print("Matrix Addition:")
for row in result_addition:
    print(row)

# Matrix subtraction
result_subtraction = subtract_matrices(matrix_a, matrix_b)
print("\nMatrix Subtraction:")
for row in result_subtraction:
    print(row)

# Matrix multiplication
result_multiplication = multiply_matrices(matrix_a, matrix_b)
print("\nMatrix Multiplication:")
for row in result_multiplication:
    print(row)

# Matrix transpose
result_transpose = transpose_matrix(matrix_a)
print("\nMatrix Transpose:")
for row in result_transpose:
    print(row)
