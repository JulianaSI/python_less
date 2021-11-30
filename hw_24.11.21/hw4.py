number = int(input('Введите целое положительное число: '))
a = 0
while number > 0:
    if number % 10 > a:
        a = number % 10
        if a == 9:
            break
    number //= 10
print(f'Наибольшая цифра числа: {a}')
