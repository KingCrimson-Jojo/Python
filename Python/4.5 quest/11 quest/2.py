one_dim_array_10 = [1] * 10 
print("Одномерный массив длины 10:", one_dim_array_10)

one_dim_array_55 = [1] * 55
print("Одномерный массив длины 55:", one_dim_array_55)

matrix = [[1 for _ in range(4)] for _ in range(3)]
print("Матрица 3x4:")
for row in matrix:
  print(row)

three_dim_array = [[[1 for _ in range(5)] for _ in range(4)] for _ in range(2)]
print("Трёхмерный массив 2x4x5:")
for i in range(2):
  for j in range(4):
    print(three_dim_array[i][j])