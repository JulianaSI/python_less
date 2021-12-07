def sum_nums(nums_str, stop):
    nums_list = nums_str.split(' ')
    sum_list = 0
    for i in nums_list:
        if i == stop:
            break
        sum_list +=int(i)

    return sum_list


stopper = '#'
finished = False
s = 0
while not finished:
    nums_str_user = input('Введите строку чисел разделенных пробелом: ')
    s += sum_nums(nums_str_user, stopper)
    finished = stopper in nums_str_user
    print(f'Сумма = {s}')

#Полностью решение Ваше. К сожалению, нет времени пробовать придумать свое решение, но я отработаю эту задачу с наставником. Напишу свой вариант, хоть он может быть не оптимальным.
