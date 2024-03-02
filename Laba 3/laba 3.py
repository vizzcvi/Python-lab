counter = 0
#Первый вопрос
answer = input("Столица России?\n")
if answer == "Москва" or answer == "москва":
 counter = counter + 1
 print("вы ответили верно")
else:
 print("вы ответили не верно")
#Второй вопрос
answer = input("Какой язык мы изучаем?\n")
if answer == "Python" or answer == "Пайтон":
 counter = counter + 1
 print("вы ответили верно")
else:
 print("вы ответили не верно") 
# Третий вопрос
answer = input("Столица Франции?\n")
if answer == "Париж" or answer == "париж":
    counter = counter + 1
    print("вы ответили верно")
else:
    print("вы ответили не верно")

# Четвертый вопрос
radius = float(input("Введите радиус круга:\n"))
area = 3.14 * (radius ** 2)
answer = float(input("Какая площадь круга с данным радиусом?\n"))
if answer == area:
    counter = counter + 1
    print("вы ответили верно")
else:
    print("вы ответили не верно")

print(f"вы набрали баллов {counter}")
