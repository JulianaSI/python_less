my_list = input('Введите значения для списка через пробел: ')
my_list_2 = my_list.split()
my_list_3 = len(my_list_2)
i=0
if my_list_3 > 1:
    while i < my_list_3 - 1:
        a_2 = my_list_2[i]
        my_list_2[i] = my_list_2[i+1]
        my_list_2[i + 1] = a_2
        i = i + 2
print(my_list_2)

# Это решение скопировала у Вас, чтобы попробовать написать код.