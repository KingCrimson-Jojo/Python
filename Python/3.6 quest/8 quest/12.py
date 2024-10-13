count = 0
number = int(input("Введите число: "))

while number < 10:
  count += 1
  number = int(input("Введите число: "))

print(f"Введено {count} чисел.")