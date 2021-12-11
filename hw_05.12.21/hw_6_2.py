from itertools import cycle, count

n = int(input('Укажите начальное число: '))
a = int(input('Укажите предельное значение: '))
my_counter = count(n, 1)
for i in range(a - n + 1):
    print(next(my_counter), end=" ")

my_list = my_counter
my_cycle = cycle(my_list)
for i in range(a):
    print(next(my_cycle), end=" ")

# Честно говоря, во второй части не смогла понять что должно быть на выходе.
# Предыдущий список плюс хвостик из новых элементов, количество которых равно введенному второму числу или нет?..
