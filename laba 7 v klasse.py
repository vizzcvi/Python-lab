import random

botNumber = random.randint(1, 10)
playerNumber = int(input("Введите число: "))
print(botNumber)
while playerNumber != botNumber:
    if playerNumber > botNumber:
        if playerNumber - botNumber <= 2:
            print("Тепло")
        else:
            print("Холодно")
        print("Ты не угадал, моё число меньше твоего")
    else:
        if botNumber - playerNumber <= 2:
            print("Тепло")
        else:
            print("Холодно")
        print("Ты не угадал, моё число больше твоего")

    playerNumber = int(input("Введите число: "))

print(f"Ты угадал, моё число: {botNumber}")
