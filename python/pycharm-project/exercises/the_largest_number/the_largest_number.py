#!/usr/bin/env python3
#-*-coding: utf-8-*-

a = (input ("Введите, первое число: "))
b = (input ("Введите, второе число: "))
c = (input ("Введите, третье число: "))

if (a != 0 or b != 0 or b != 0):
    if (a >= b and a >= c):
      n = a;
    if (b >= a and b >= c):
      n = b;
    if (c >= a and c >= b):
      n = c
    print (n, "является самым большим числом")