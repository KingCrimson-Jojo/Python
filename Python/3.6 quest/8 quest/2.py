sum = 0
number = int(input("Введите число: "))

while number < 0:
  sum += number
  number = int(input("Введите число: "))

print(f"Сумма отрицательных чисел: {sum}")