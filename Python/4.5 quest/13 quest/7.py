import numpy as np
import math

t_values_1 = np.arange(-10, 11, 1)
y_values_1 = 4 * np.sin(np.pi * t_values_1 + np.pi / 8) - 1
print("t ∈ [-10; 10], шаг 1:")
print(f"t: {t_values_1}")
print(f"y: {y_values_1}")

t_values_0_25 = np.arange(-10, 10.25, 0.25)
y_values_0_25 = 4 * np.sin(np.pi * t_values_0_25 + np.pi / 8) - 1
print("t ∈ [-10; 10], шаг 0.25:")
print(f"t: {t_values_0_25}")
print(f"y: {y_values_0_25}")