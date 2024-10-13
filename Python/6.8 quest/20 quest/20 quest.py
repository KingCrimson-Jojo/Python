import os

current_directory = os.getcwd()


file_path = os.path.join(current_directory, "6.8 quest", "20 quest", "Зачёт.txt")


def find_grade(file_path, last_name):
  with open(file_path, "r") as file:

    lines = file.readlines()


    for line in lines:
      if last_name in line:

        grade = line.split("\t")[-1] 
        return grade
  
  return "Оценка не найдена"

student_last_name = input("Введите фамилию ученика: ")

grade = find_grade(file_path, student_last_name)

print(f"Оценка ученика {student_last_name}: {grade}")