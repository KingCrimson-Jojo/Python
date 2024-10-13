#a
School = {"1а": 25, "1б": 28, "2в": 22, "3г": 26, "4д": 24}
print(School)

#b
class_name = input("Введите название класса: ")
if class_name in School:
    print(f"В классе {class_name} {School[class_name]} человек.")
else:
    print("Такого класса не существует.")

#c
School["1а"] = 27
School["2в"] = 20
School["3г"] = 25
print(School)

#d
School["5е"] = 23
School["6ж"] = 21
print(School)

#e
del School["4д"]
print(School)