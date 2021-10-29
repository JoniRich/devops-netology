#!/usr/bin/env python3
# -*-coding: utf-8-*-
# Задача выполняется в качестве домашней работы по программированию на Python
# Задача выполнить необходмо в HackerRang ссылка на задачу https://www.hackerrank.com/challenges/py-if-else/problem
# Учитывая целое число,выполните следующие условные действия:
# Если  нечетное, напечатайте Weird
# Если  является четным и находится в инклюзивном диапазоне 2  к 5 , Распечатать Not Weird
# Если  является четным и находится в инклюзивном диапазоне 6 к , 20 Распечатать Weird
# Если  даже и больше, чем 20 , Распечатать Not Weird

# рабочая прога на ХакерРанк https://www.hackerrank.com/challenges/py-if-else/problem

# n = int(input("Введите целое число :")) и так тоже работает а на сайте только вот так: n = int(input().strip())

# File task 1 hackerrank author: Evgeny Vasilyev (JoniRich)

n = int(input("Введите число: ").strip())

if 1 <= n <= 100:
    result = n % 2
    if result != 0:
        print("Weird")
    elif 5 >= n >= 2:
        print("Not Weird")
    elif 6 <= n <= 20:
        print("Weird")
    elif 20 <= n <= 100:
        print("Not Weird")
exit(0)
