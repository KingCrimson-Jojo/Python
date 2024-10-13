#a
list1 = list(range(0, 100, 10))
list2 = list(range(0, 100, 10))

#b
second_element = list1[1]
print(second_element)

#c
list2[-1] = 200
print(list2)

#d
combined_list = list1 + list2
print(combined_list)

#e
slice_list = combined_list[3:11]
print(slice_list)

#f
slice_list.extend([300, 400])
print(slice_list)

#g
min_value = min(combined_list)
max_value = max(combined_list)
print(f"Минимальное значение: {min_value}, Максимальное значение: {max_value}")