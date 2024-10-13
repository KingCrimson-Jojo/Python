import numpy as np
import os

def calculate_determinant():
    
    folder_name = "Распределения"
    file_name = "равномерное.txt"  

    file_path = os.path.join(folder_name, file_name)

    
    with open(file_path, "r") as f:
        data = [line.strip().split() for line in f]

    
    matrix = np.array(data, dtype=float)

    
    determinant = np.linalg.det(matrix)

    print(f"Определитель матрицы из файла {file_name}: {determinant}")

if __name__ == "__main__":
    calculate_determinant()