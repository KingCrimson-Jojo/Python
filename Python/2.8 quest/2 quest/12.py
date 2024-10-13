x = int(input("Введите расстояние до первого столба (в метрах): "))
y = int(input("Введите расстояние между столбами (в метрах): "))
z = int(input("Введите длину вашего шага (в метрах): "))
n = int(input("Введите количество шагов: "))

total_distance = z * n
passed_distance = total_distance - x
columns_passed = passed_distance // y

print(f"Вы пройдете мимо {columns_passed} столбов.")