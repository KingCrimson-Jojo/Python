A = int(input("Введите количество копеек: "))

rubles = A // 100
A %= 100

grivnas = A // 10
A %= 10

altyns = A // 3
A %= 3

polushki = A // 0.25
A %= 0.25

print(f"Разложение суммы в копейках: {rubles} рублей + {grivnas} гривен + {altyns} алтынов + {polushki} полушек")