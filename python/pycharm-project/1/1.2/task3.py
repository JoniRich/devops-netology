#!/usr/bin/env python3


# Разработать приложение для определения знака зодиака по дате рождения.
# Пример:
#
# Введите месяц: март
# Введите число: 6
#
# Вывод:
# Рыбы

month = str(input("Введите месяц вашего рождения:"))

numb = int(input("Введите день вашего рождения:"))

if numb > 31:
    print("не верная дата!")
elif (month == "март" and numb >= 21) | (month == "апрель" and numb <= 19):
    print("ты - овен")
elif (month == "апрель" and numb >= 20) | (month == "май" and numb <= 20):
    print("ты - телец")
elif (month == "май" and numb >= 21) | (month == "июнь" and numb <= 21):
    print("ты - близнец")
elif (month == "июнь" and numb >= 22) | (month == "июль" and numb <= 22):
    print("ты - рак")
elif (month == "июль" and numb >= 23) | (month == "август" and numb <= 22):
    print("ты - лев")
elif (month == "август" and numb >= 23) | (month == "сентябрь" and numb <= 22):
    print("ты - дева")
elif (month == "сентябрь" and numb >= 23) | (month == "октябрь" and numb <= 23):
    print("ты - весы")
elif (month == "октябрь" and numb >= 24) | (month == "ноябрь" and numb <= 22):
    print("ты - скорпион")
elif (month == "ноябрь" and numb >= 23) | (month == "декабрь" and numb <= 21):
    print("ты - стрелец")
elif (month == "декабрь" and numb >= 22) | (month == "январь" and numb <= 20):
    print("ты - козерог")
elif (month == "январь" and numb >= 21) | (month == "февраль" and numb <= 18):
    print("ты - водолей")
elif (month == "февраль" and numb >= 19) | (month == "март" and numb <= 20):
    print("ты - рыба")

else:
    print("по козерогу ты гороскоп!")

exit(0)
