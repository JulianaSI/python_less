full_name = input('Введите ФИО менеджера: ')
zakaz = int(input('Введите количество обработанных заказов: '))
summa_zak = float(input('Введите общую стоимость заказов: '))
result = summa_zak / zakaz
result = f'Средняя стоимость одного заказа {result:.2f} руб.'
print(full_name)
print(zakaz, ' (количество заказов)')
print(summa_zak, ' руб. (общая стоимость заказов)')
print(result)
