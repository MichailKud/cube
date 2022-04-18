import random

b = int(input("на какое число вы ставите(от 1 до 6)?"))
a = random.randint(1,6)
if (b > 6):
  print("Выбирите число из перечня")

elif (a == b):
  print("Выигрыш: ")

elif (a != b):
  print("Проигрыш: ")
