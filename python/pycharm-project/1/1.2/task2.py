#!/usr/bin/env python3

# Задача №2
# На лекции мы рассматривали пример для военкомата.
# Сейчас мы знаем про его рост. Расширить это приложение следующими условиями:
#
# Проверка на возраст призывника.
# Количество детей.
# Учится ли он сейчас.

# Условие:
# если парню 18 и меньше 27 он идет в армию
# если рост < 180 он идет в десант
# если рост >=170 танкисты
# от 170-180 на флот, если учится или есть 2 ребенка ребенок то идет с отсрочкойе

age = int(input("Введите возраст:"))
height = int(input("Введите ваш рост:"))
student = str(input("Вы студент? y/n :"))
children = int(input("Сколько у вас детей?:"))

if age > 27 | age < 18:

    print("Не годен к службе по возрасту")

else:

    print("Годен к службе!")

    if height >= 180:

        print("Вы идете служить в десант")

    elif 180 > height > 170:

        print("Вы идете служить во флот")

    else:
        print("Вы идете служить в танкисты")

    if student == "y":

        print("Вы не можете идти на службу пока учитесь")

    elif student == "n":

        print("Вы не учитись и можете служить!")

    else:
        print("не верный ввод данных")

    if children <= 1:

        print("у вас нет дитей или один ребенок вы можете служить")

    else:

        print("у вас более одного ребенка вы не можете служить")

exit(0)
