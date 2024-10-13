import numpy as np

matrix = [[1, 1, 1, 1, 1],
          [2, 2, 2, 2, 2],
          [3, 3, 3, 3, 3],
          [4, 4, 4, 4, 4],
          [5, 5, 5, 5, 5]]

if len(matrix) > 1 and len(matrix[0]) > 1:
  print("Массив двумерный.")
else:
  print("Массив не двумерный.")

vector = np.arange(1, 6)

result = np.array(matrix) + vector
print("Результат сложения матрицы и вектора:", result)

max_element = np.max(result)
min_element = np.min(result)
print(f"Максимальный элемент: {max_element}, Минимальный элемент: {min_element}")

row_sums = np.sum(result, axis=1)
print("Сумма элементов по каждой строке:", row_sums)

np.savetxt("matrix_result.txt", result, fmt="%d")
np.savetxt("vector.txt", vector, fmt="%d")