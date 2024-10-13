import math

x = float(input("Введите значение x: "))

if x > 0:
    y = math.sin(2 * x)
elif x == 0:
    y = 0
else:
    y = 1 + 2 * math.sin(x ** 2)

print(f"Значение функции y(x): {y}")