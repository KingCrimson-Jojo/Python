import numpy as np
import matplotlib.pyplot as plt


noise = np.random.normal(-2, 0.25, 10000)


plt.hist(noise, bins=50, edgecolor='black')
plt.xlabel('Значение')
plt.ylabel('Частота')
plt.title('Гистограмма нормального шума')
plt.show()