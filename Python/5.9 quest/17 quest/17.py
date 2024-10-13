import numpy as np
import matplotlib.pyplot as plt

t_values = np.linspace(-1, 1, 100)
omega_values = [2 * np.pi * i for i in range(2, 9)]


fig, ax = plt.subplots()
for i, omega in enumerate(omega_values):
  y_values = np.sin(omega * t_values)
  ax.plot(t_values, y_values, label=f"ω = {omega:.2f}")

ax.set_xlabel("t")
ax.set_ylabel("y")
ax.set_title("Семейство синусоид y = sin(ωt)")
ax.legend()
ax.grid(True)
plt.show()


fig, axes = plt.subplots(nrows=len(omega_values), figsize=(5, 15))
for i, omega in enumerate(omega_values):
  y_values = np.sin(omega * t_values)
  axes[i].plot(t_values, y_values)
  axes[i].set_title(f"ω = {omega:.2f}")
  axes[i].grid(True)
plt.tight_layout()
plt.show()


fig, axes = plt.subplots(nrows=len(omega_values) // 2, ncols=2, figsize=(10, 10))
for i, omega in enumerate(omega_values):
  y_values = np.sin(omega * t_values)
  row = i // 2
  col = i % 2
  axes[row, col].plot(t_values, y_values)
  axes[row, col].set_title(f"ω = {omega:.2f}")
  axes[row, col].grid(True)
plt.tight_layout()
plt.show()


fig, axes = plt.subplots(nrows=len(omega_values) // 3 + 1, ncols=3, figsize=(15, 10))
for i, omega in enumerate(omega_values):
  y_values = np.sin(omega * t_values)
  row = i // 3
  col = i % 3
  axes[row, col].plot(t_values, y_values)
  axes[row, col].set_title(f"ω = {omega:.2f}")
  axes[row, col].grid(True)
plt.tight_layout()
plt.show()


fig, axes = plt.subplots(nrows=1, ncols=len(omega_values), figsize=(20, 5))
for i, omega in enumerate(omega_values):
  y_values = np.sin(omega * t_values)
  axes[i].plot(t_values, y_values)
  axes[i].set_title(f"ω = {omega:.2f}")
  axes[i].grid(True)
plt.tight_layout()
plt.show()


for i, omega in enumerate(omega_values):
  y_values = np.sin(omega * t_values)
  plt.figure()
  plt.plot(t_values, y_values)
  plt.xlabel("t")
  plt.ylabel("y")
  plt.title(f"ω = {omega:.2f}")
  plt.grid(True)
  plt.savefig(f"graph_{i}.png")
  plt.show()