import os
import matplotlib.pyplot as plt

def plot_histograms():
    
    folder_name = "Распределения"


    os.chdir(folder_name)


    for file_name in os.listdir():
        if file_name.endswith(".txt"):
            data = []
            with open(file_name, "r") as f:
                for line in f:
                    data.append(float(line.strip()))


            plt.hist(data, bins=20)
            plt.xlabel("Значение")
            plt.ylabel("Частота")
            plt.title(f"Гистограмма {file_name[:-4]}")


            plt.savefig(file_name[:-4] + ".png") 
            plt.close()

if __name__ == "__main__":
    plot_histograms()