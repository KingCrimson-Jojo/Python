import numpy as np

x_values_0_01 = np.arange(-2, 2.01, 0.01)
y_values_0_01 = x_values_0_01 ** 3
print("x ∈ [-2; 2], шаг 0.01:")
print(f"x: {x_values_0_01}")
print(f"y: {y_values_0_01}")

x_values_0_1 = np.arange(-2, 2.1, 0.1)
y_values_0_1 = x_values_0_1 ** 3
print("x ∈ [-2; 2], шаг 0.1:")
print(f"x: {x_values_0_1}")
print(f"y: {y_values_0_1}")

x_values_0_25 = np.arange(-2, 2.25, 0.25)
y_values_0_25 = x_values_0_25 ** 3
print("x ∈ [-2; 2], шаг 0.25:")
print(f"x: {x_values_0_25}")
print(f"y: {y_values_0_25}")