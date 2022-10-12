# 0004 – Задайте список из N элементов, заполненных числами из промежутка [-N, N].
# Найдите произведение элементов на указанных позициях. Позиции хранятся в файле file.txt в одной строке одно число.

from random import randint

try:
    number = int(input('Введите N: '))
except ValueError:
    print('Допускаются только натуральные числа. Программа завершает работу... ')
    exit()
if number < 1:
    print('Допускаются только положительные числа. Программа завершает работу... ')
    exit()

array = []
for i in range(number):
    array.append(randint(-number, number))
print(f'Список случайных {number} чисел от {-number} до {number}: \n {array}')

file_name = open('file.txt', 'r')

print('Все индексы из файла file.txt: ')
print(*(line.strip() for line in file_name.readlines()))

multiply = 1
file_name.seek(0)
indexess = []
for line in file_name.readlines():
    if 0 <= int(line) < number:
        indexess.append(int(line))
        multiply *= array[int(line)]

print(f'Подходящие индексы диапазона от 0 до {number - 1} из файла file.txt: ', indexess)
print('Произведение элементов: ', multiply if indexess != [] else 0)

file_name.close
