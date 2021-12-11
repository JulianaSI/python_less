def fact(end):
    n_fact = 1
    for i in range(1, end + 1):
        n_fact *= i
    yield n_fact

n = int(input('Введите число, факториал которого необходимо вычислить: '))
for el in fact(n):
    print(f'{n}! = {el}')
