def my_func(num_1, num_2):
    a = (num_1**num_2)
    return a

x = int(input('Введите действительное положительное число: '))
y = int(input('Введите целое отрицательное число: '))
result = my_func(x, y)
print('%.4f' % result)
