import random


n = int(input("Введите ваш номер в списке группы по алфавиту: "))
m = int(input("Введите количество задач в задании: "))


task_number = (n - 1) % m + 1
print(f"Вам необходимо выполнить задание № {task_number}")