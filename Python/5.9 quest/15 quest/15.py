import numpy as np
import matplotlib.pyplot as plt

t_values = np.arange(-10, 11, 1)
y_values = 4 * np.sin(np.pi * t_values + np.pi / 8) - 1 

plt.plot(t_values, y_values, color='red', linestyle='--', marker='o', label="4 sin(πt + π/8) - 1")

plt.xticks(np.arange(-10, 11, 2))

plt.grid(True)

plt.xlabel("t")
plt.ylabel("y")
plt.title("График функции 4 sin(πt + π/8) - 1")

plt.legend()

plt.savefig("graph.png")
plt.savefig("graph.jpg")
plt.savefig("graph.pdf")
plt.savefig("graph.eps")
plt.savefig("graph.svg")
plt.savefig("graph.svgz") 

plt.show()