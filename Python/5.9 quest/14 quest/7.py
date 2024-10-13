import numpy as np
import matplotlib.pyplot as plt


t_values_1 = np.arange(-10, 11, 1)
y_values_1 = 4 * np.sin(np.pi * t_values_1 + np.pi / 8) - 1


plt.plot(t_values_1, y_values_1, label="4 sin(πt + π/8) - 1")
plt.xlabel("t")
plt.ylabel("y")
plt.title("График функции 4 sin(πt + π/8) - 1")
plt.legend()
plt.grid(True)
plt.show()