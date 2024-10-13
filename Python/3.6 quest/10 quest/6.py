import random

while True:
  choice = int(input("Введите 0 для орла, 1 для решки, любое другое число для выхода: "))

  if choice == 0:
    user_choice = "орёл"
  elif choice == 1:
    user_choice = "решка"
  else:
    break

  coin_side = random.choice(["орёл", "решка"])

  print(f"Выпал {coin_side}")

  if user_choice == coin_side:
    print("Вы выиграли!")
  else:
    print("Вы проиграли!")