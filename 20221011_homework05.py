# 0005 – Реализуйте алгоритм перемешивания списка.

from random import randint

try:
    number = int(input('Введите размер списка: '))
except ValueError:
    print('Допускаются только натуральные числа. Программа завершает работу... ')
    exit()
if number < 1:
    print('Допускаются только положительные числа. Программа завершает работу... ')
    exit()

array = []
for i in range(number):
    array.append(i)
print(f'Упорядоченный список: \n {array}')

for i in range(number):

    random_index = randint(0, number - 1)
    while random_index == i:  # исключает совпадение текущего индекса с новым случайным
        random_index = randint(0, number - 1)

    temp = array[i]
    array[i] = array[random_index]
    array[random_index] = temp

print('Перемешанный список: ', array)
