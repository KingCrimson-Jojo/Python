import cmath

p = float(input("Введите значение коэффициента p: "))
q = float(input("Введите значение коэффициента q: "))

D = (q / 2)**2 + (p / 3)**3

if D >= 0:
    u = (-(q / 2) + D**0.5)**(1/3)
    v = (-(q / 2) - D**0.5)**(1/3)
    y1 = u + v
    y2 = -0.5 * (u + v) + cmath.sqrt(3) / 2 * (u - v) * 1j
    y3 = -0.5 * (u + v) - cmath.sqrt(3) / 2 * (u - v) * 1j
    print(f"Корни уравнения: y1 = {y1}, y2 = {y2}, y3 = {y3}")

else:
    phi = cmath.acos(-(q / 2) / ((-p / 3)**1.5))
    y1 = 2 * ((-p / 3)**0.5) * cmath.cos(phi / 3)
    y2 = 2 * ((-p / 3)**0.5) * cmath.cos((phi + 2 * cmath.pi) / 3)
    y3 = 2 * ((-p / 3)**0.5) * cmath.cos((phi + 4 * cmath.pi) / 3)
    print(f"Корни уравнения: y1 = {y1}, y2 = {y2}, y3 = {y3}")