import numpy as np
import matplotlib.pyplot as plt


a = -4
b = 4
n = 100  
sigma = 1 


x = np.linspace(a, b, n)
y = x**2 - x - 6 + np.random.normal(0, sigma, n)


coeffs = np.polyfit(x, y, 2)
y_approx = np.polyval(coeffs, x)


error = np.mean(np.abs(y - y_approx))


plt.plot(x, y, 'o', label='Данные с шумом')
plt.plot(x, y_approx, label='Аппроксимация')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Аппроксимация параболы полиномом второй степени')
plt.legend()
plt.show()

print(f'Ошибка аппроксимации: {error}')