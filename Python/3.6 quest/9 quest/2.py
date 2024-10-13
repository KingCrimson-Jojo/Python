a = int(input("Введите число a: "))
b = int(input("Введите число b: "))

sum = 0
for i in range(a, b + 1):
  if i % 2 == 0:
    sum += i

print(f"Сумма четных чисел в диапазоне от {a} до {b}: {sum}")