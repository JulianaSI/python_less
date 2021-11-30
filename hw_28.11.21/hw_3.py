my_dict = {12:'winter', 1:'winter', 2:'winter', 3:'spring', 4:'spring', 5:'spring', 6:'summer', 7:'summer', 8:'summer', 9:'autumn', 10:'autumn', 11:'autumn'}
a = int(input('Введите целое число от 1 до 12: '))
print(f'This is {my_dict.get(a)}')

# 'winter': [12, 1, 2], 'spring' : [3, 4, 5], 'summer' : [6, 7, 8], 'autumn' : [9, 10, 11],