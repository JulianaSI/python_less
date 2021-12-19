from sys import argv

print(argv)
num_1 = int(argv[1])    # выработка в часах
num_2 = int(argv[2])    # ставка в часах
num_3 = int(argv[3])    # премия
print(num_1 * num_2 + num_3)
