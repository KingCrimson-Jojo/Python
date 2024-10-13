import numpy as np
import matplotlib.pyplot as plt


a = -4
b = 4
n = 100 
sigma = 1 
num_rows = 5


x = np.linspace(a, b, n)
y_rows = []
for _ in range(num_rows):
    y_rows.append(x**2 - x - 6 + np.random.normal(0, sigma, n))


y_mean = np.mean(y_rows, axis=0)
y_std = np.std(y_rows, axis=0)


plt.errorbar(x, y_mean, yerr=y_std, fmt='o-', label='Средние значения')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Средние значения с планками погрешностей')
plt.legend()
plt.show()