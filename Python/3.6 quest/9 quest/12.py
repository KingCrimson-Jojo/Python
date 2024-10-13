b = int(input("Введите число b: "))

sum = 0
for i in range(10, b + 1):
  sum += i

print(f"Сумма всех целых чисел от 10 до {b}: {sum}")