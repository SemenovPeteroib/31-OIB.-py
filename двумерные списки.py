import random
matrix_1 = [[random.randint(-50, 100) for _ in range(10)] for _ in range(10)]
matrix_2 = [[random.randint(-50, 100) for _ in range(10)] for _ in range(10)]
print("Matrix 1:")
for row in matrix_1:
    print(row)
print("\nMatrix 2:")
for row in matrix_2:
    print(row)
matrix_3 = [[0 for _ in range(10)] for _ in range(10)]
for i in range(10):
    for j in range(10):
        matrix_3[i][j] = matrix_1[i][j] + matrix_2[i][j]
print("\nMatrix 3 (matrix_1 + matrix_2):")
for row in matrix_3:
    print(row)
