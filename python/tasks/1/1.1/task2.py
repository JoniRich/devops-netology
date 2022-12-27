#!/usr/bin/env python3
#-*-coding: utf-8-*-

#Программа запрашивает у пользователя длину стороны квадрата и выводит его периметр и площадь.
#Сразу после этого пользователю предлагается ввести длину и ширину прямоугольника, для которого рассчитывается периметр и площадь.
#Обратите внимание, что программа должна работать корректно при любых введённых значениях длины и ширины фигуры.

side_square = int(input('Введите размер стороны квадрата:'))
perimeter_square = 4 * side_square
area_square = side_square ** 2
print('Периметр', perimeter_square)
print('Площадь', area_square)

length_rectangle = int(input('Введите длину прямоугольника:'))
width_rectangle = int(input('Введите ширину прямоугольника:'))

perimeter_rectangle = 2 * (length_rectangle + width_rectangle)
area_rectangle = length_rectangle * width_rectangle
print('Периметр', perimeter_rectangle)
print('Площадь', area_rectangle)