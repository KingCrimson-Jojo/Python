surname = input("Введите мужскую фамилию: ")
if surname[-1] == 'в':
    surname = surname[:-1] + 'а'
else:
    surname = surname + 'а'
print(f"Женская фамилия: {surname}")