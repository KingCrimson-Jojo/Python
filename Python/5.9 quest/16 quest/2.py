import numpy as np
import matplotlib.pyplot as plt


t_values = np.linspace(-1, 1, 100)


omega_values = [2 * np.pi * i for i in range(2, 9)]


for i, omega in enumerate(omega_values):
  y_values = np.sin(omega * t_values)
  plt.plot(t_values, y_values, label=f"ω = {omega:.2f}")


plt.xlabel("t")
plt.ylabel("y")
plt.title("Семейство синусоид y = sin(ωt)")
plt.legend()
plt.grid(True)


plt.show()