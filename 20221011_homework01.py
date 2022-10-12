# 0001 – Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# Пример:
# 6782 -> 23
# 0,56 -> 11


try:
    number = float(input('Введите число: '))
    number = str(number)
except ValueError:
    print('Неверный ввод числа. Программа завершает работу ')
    exit()
    
summa = 0
for i in range(len(number)):
    if number[i] != '.' and number[i] != '-':
        summa += int(number[i])
print(f'Сумма цифр числа {number} равна: {summa}')
