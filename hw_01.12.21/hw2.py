def user_info(name, surname, year, city, email, phone):
    return f'{name} {surname} {year} {city} {email} {phone}'

n = input('Name: ')
s = input('Surname: ')
y = input('Year: ')
c = input('City: ')
e = input('E-mail: ')
p = input('Phone: ')
result = user_info(name=n, surname=s, year=y, city=c, email=e, phone=p)
print(result)

# Решение списано у Вас. Метод решения мне понятен. Считаю его оптимальным, поэтому не стала что-то сложное выдумывать.
