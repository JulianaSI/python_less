def my_func(x, y):
    z = 1
    for i in range(y * -1):
        z *= x
    return 1 / z

x = int(input('Введите действительное положительное число: '))
y = int(input('Введите целое отрицательное число: '))
print('%.4f' % my_func(x, y))

# Решение взято Ваше. Честно признаюсь, допускала ошибку, ставя return на одном уровне с z. Поставив на уровень с for, результат получился правильным. Ошибку осознала.
