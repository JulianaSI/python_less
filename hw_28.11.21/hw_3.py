my_dict = {12:'winter', 1:'winter', 2:'winter', 3:'spring', 4:'spring', 5:'spring', 6:'summer', 7:'summer', 8:'summer', 9:'autumn', 10:'autumn', 11:'autumn'}
a = int(input('Введите целое число от 1 до 12: '))
print(f'This is {my_dict.get(a)}')

# Добрый день! Дамир, не знала как правильно задать вопрос, чтобы не отнимать у Вас время, поэтому решила здесь написать в виде комментария
# Я зациклилась на варианте решения задачи с помощь вложенных списков. Это как идея-фикс, но не знаю как правильно осуществить и реально ли это.
# Итак, я хотела создать список с вложенными списками, т.о. у меня в каждом индексе были бы месяцы определенного сезона.
# И словарь, в котором цифра индекса (стала бы ключом) равнялась бы сезону. Далее пользователь вводит значение, которое проверяется во вложенных списках.
# Затем определяется индекс вложенного списка и выводим на печать значение из словаря этого сезона.
# В общем, хотела оптимальный вариант именно для этой задачи придумать. Понимаю, что во вложенных списках должны быть уникальные значения,
# чтобы правильно определить индекс, поэтому этот метод хотела применить в данном случае.