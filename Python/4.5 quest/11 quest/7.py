import math

array = []
for i in range(-15 * 12, 16 * 12):
  array.append(i * math.pi / 12)

print("Массив-диапазон от -15π до 15π с шагом π/12:", array)