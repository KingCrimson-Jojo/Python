points = int(input("Введите количество очков, полученных командой: "))

if points == 3:
    result = "Выигрыш"
elif points == 1:
    result = "Ничья"
else:
    result = "Проигрыш"

print(f"Результат игры: {result}")