import numpy as np
import os

def create_files():

    folder_name = "Распределения"


    if not os.path.exists(folder_name):
        os.makedirs(folder_name)


    with open(os.path.join(folder_name, "равномерное.txt"), "w") as f:

        matrix = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
        for row in matrix:
            f.write(" ".join(str(x) for x in row) + "\n")


    with open(os.path.join(folder_name, "нормальное.txt"), "w") as f:
  
        b = np.array([10, 20, 30])
        for value in b:
            f.write(str(value) + "\n")

def solve_linear_equations():

    folder_name = "Распределения"


    with open(os.path.join(folder_name, "равномерное.txt"), "r") as f:
        A = np.array([[float(x) for x in line.split()] for line in f])


    with open(os.path.join(folder_name, "нормальное.txt"), "r") as f:
        b = np.array([float(line.strip()) for line in f])

 
    x = np.linalg.solve(A, b)


    with open(os.path.join(folder_name, "корни.txt"), "w") as f:
        for i in x:
            f.write(str(i) + "\n")

    print("Корни уравнений записаны в файл корни.txt")

if __name__ == "__main__":
    create_files()  
    solve_linear_equations()  