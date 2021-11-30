second = int(input('Введите время в секундах: '))
if second < 60:
    print(f'Формат чч:мм:сс равен 00:00:{second:02}')
elif second < 3600:
    print(f'Формат чч:мм:сс равен 00:{second // 60:02}:{second % 60:02}')
else:
    print(f'Формат чч:мм:сс равен {second // 3600:02}:{(second % 3600) // 60:02}:{second % 60:02}')
