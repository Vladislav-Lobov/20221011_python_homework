# 0003 – Задайте список из n чисел последовательности (1 + 1 / n) ** n и выведите на экран их сумму.
# Пример:
# 1 -> 2.0
# 2 -> 4.25
# 3 -> 6.62037037037037

def get_n(n):
    return (1 + 1 / n) ** n


try:
    number = int(input('Введите N: '))
except ValueError:
    print('Допускаются только натуральные числа. Программа завершает работу... ')
    exit()
if number < 1:
    print('Допускаются только положительные числа. Программа завершает работу... ')
    exit()

result = [2.0]
for i in range(1, number):
    result.append(result[i - 1] + get_n(i + 1))
print(result)
