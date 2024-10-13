#a
students_number = int(input("Введите количество учеников в группе: "))
tuple1 = tuple(range(1, students_number + 1))
tuple2 = ("Фетисов", "Михайлов", "Мингазов", "Мельников", "Бормотов", "Кулёк", "Дрочена", "Зайцев", "Павлючков", "Семисаженов")

#b
surname_5 = tuple2[4]
print(f"Фамилия студента с номером 5: {surname_5}")

#c
element_5 = tuple2[4]
print(f"Элемент под номером 5: {element_5}")

#d
combined_tuple = tuple1 + tuple2
print(combined_tuple)

#e
slice_tuple = combined_tuple[3:10]
print(slice_tuple)