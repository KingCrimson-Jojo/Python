#2.1
x = int(input("Введите значение x: "))
y = int(input("Введите значение y: "))

result = x**2 - y**2 > 64

print(f"Значение логического выражения: {result}")

#2.2
print("Таблица истинности:")
print("X | Y | Z | Y или (X и не Y или Z)")
print("-" * 40)
for x in [True, False]:
    for y in [True, False]:
        for z in [True, False]:
            result = y or (x and not y or z)
            print(f"{x} | {y} | {z} | {result}")

#2.3
x = int(input("Введите число X: "))
condition = x > 10 and x < 20

print(f"Логическое выражение: {condition}")