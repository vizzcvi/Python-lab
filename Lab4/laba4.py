age = int(input("Введите возраст: "))
if age > 0 and age <= 10:
    print("Вы ребёнок")
elif age > 10 and age <= 16:
    print("Вы подросток")
elif age > 16 and age < 22:
    print("Вы молодой взрослый")
elif age >= 22 and age < 30:
    print("Вы молодой")
elif age >= 30 and age < 50:
    print("Вы взрослый")
else:
    print("Возраст введён неверно!")
