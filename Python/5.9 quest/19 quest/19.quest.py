import numpy as np
import matplotlib.pyplot as plt


def function(x, y):
  return x**2 + y**2 + x


x = np.linspace(-3, 3, 100) 
y = np.linspace(-3, 3, 100) 
X, Y = np.meshgrid(x, y) 


Z = function(X, Y)


plt.figure(figsize=(10, 10))
plt.contourf(X, Y, Z, levels=20)
plt.colorbar()
plt.title("Закрашенная контурная диаграмма")
plt.xlabel("X")
plt.ylabel("Y")


fig = plt.figure(figsize=(10, 10))
ax = fig.add_subplot(projection='3d')
ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap='jet')
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
plt.title("Трёхмерный график")


plt.show()