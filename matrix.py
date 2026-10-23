import numpy as np # I am importing all module

N = int(input("Введите количество строк: "))
M = int(input("Введите количество столбцов: "))

# A matrix for random numbers from 0 to 9 has been created.
matrix = np.random.randint(1, 10, size=(N, M))
print(matrix)

print(" ")

# Transposing the matrix
transposedMatrix = matrix.T
print("Транспонированная матрица:")
print(transposedMatrix)

print(" ")


if N == M:
    # I calculate the determinant of matrices
    OprMatrix = np.linalg.det(matrix)
    OprTransposedMatrix = np.linalg.det(transposedMatrix)

    print(f"Определитель исходной матрицы: {round(OprMatrix, 4)}")
    print(f"Определитель транспонированной матрицы: {round(OprTransposedMatrix, 4)}")

    # Comparing identification guides
    if np.isclose(OprMatrix, OprTransposedMatrix):
        print("Определители равны")
    else:
        print("Определители не равны")
else:
    print("Ошибка: Определитель можно вычислить только для квадратной матрицы (когда количество строк равно количеству столбцов).")
