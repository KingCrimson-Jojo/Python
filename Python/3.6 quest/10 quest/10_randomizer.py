n = int(input("Введите ваш порядковый номер в списке группы по алфавиту: "))
task_number = (n - 1) % 8 + 1

print(f"Вам необходимо выполнить задание № {task_number}.")