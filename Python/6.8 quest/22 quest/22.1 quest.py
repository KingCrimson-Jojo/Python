import os
import random
import numpy as np
import matplotlib.pyplot as plt

def create_files():
    
    folder_name = "Распределения"

    
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)

   
    file_names = ["равномерное.txt", "нормальное.txt", "хи_квадрат.txt"]

    for file_name in file_names:
        file_path = os.path.join(folder_name, file_name)
        with open(file_path, "w") as f:
            if file_name == "равномерное.txt":
                data = [random.uniform(0, 1) for _ in range(1000)]
            elif file_name == "нормальное.txt":
                data = np.random.normal(0, 1, 1000)
            elif file_name == "хи_квадрат.txt":
                data = np.random.chisquare(df=5, size=1000)
            for value in data:
                f.write(str(value) + "\n")

if __name__ == "__main__":
    create_files()