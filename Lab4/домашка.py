rubles = float(input("Введите сумму в рублях: "))
currency = input("Выберите валюту для конвертации (доллары, евро или юани): ")

if currency == "доллары":
    exchange_rate = 91.33  # курс доллара к рублю
    result = rubles / exchange_rate
    print(f"{rubles} рублей равно {result} долларов")
elif currency == "евро":
    exchange_rate = 98.72  # курс евро к рублю
    result = rubles / exchange_rate
    print(f"{rubles} рублей равно {result} евро")
elif currency == "юани":
    exchange_rate = 12.63  # курс юаня к рублю
    result = rubles / exchange_rate
    print(f"{rubles} рублей равно {result} юаней")
else:
    print("Выбрана неверная валюта. Пожалуйста, выберите из долларов, евро или юаней.")


