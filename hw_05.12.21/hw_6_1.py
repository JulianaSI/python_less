from itertools import count

n = int(input('Укажите начальное число: '))
a = int(input('Укажите предельное значение: '))
my_counter = count(n, 1)
for i in range(a - n + 1):
    print(next(my_counter), end=" ")
