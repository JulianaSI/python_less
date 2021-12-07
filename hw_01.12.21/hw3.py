def my_func(num_1, num_2, num_3):
    sum_num = num_1 + num_2 + num_3
    return sum_num - min((num_1, num_2, num_3))

a = int(input('a = '))
b = int(input('b = '))
c = int(input('c = '))
s = my_func(a, b, c)
print(f'Сумма наибольших двух чисел = {s}')

# Решение Ваше. Малость добавила от себя.
