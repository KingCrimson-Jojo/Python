n = float(input("Введите число n: "))
i = 1
sum = 1

while sum <= n:
  i += 1
  sum += 1 / i
  
print(f"Первое число, большее n: {sum}")