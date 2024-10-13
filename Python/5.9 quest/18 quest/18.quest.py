import matplotlib.pyplot as plt

percentages = [50, 30]

categories = ["Пятёрки", "Четвёрки"]

colors = ["#008000", "#0000FF"]

plt.pie(percentages, labels=categories, colors=colors, autopct='%1.1f%%')

plt.title("Доли от общего числа студентов, сдавших сессию на \"5\" и \"4\"")

plt.show()