# 0002 – Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
# Пример:
# пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

def get_factorial(n):
    if n == 1:
        return 1
    return get_factorial(n - 1) * n


try:
    number = int(input('Введите N: '))
except ValueError:
    print('Допускаются только натуральные числа. Программа завершает работу... ')
    exit()
if number < 1:
    print('Допускаются только положительные числа. Программа завершает работу... ')
    exit()

result = []
for i in range(1, number + 1):
    result.append(get_factorial(i))

print(f'При N = {number} набор равен: ', result)
