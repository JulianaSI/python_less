with open('текст.txt', 'w') as file:
    strings = input('Введите текст построчно (окончание ввода - пустая строка):\n')
    while strings:
        file.write(f'{strings}\n')
        strings = input('Введите текст построчно (окончание ввода - пустая строка):\n')
