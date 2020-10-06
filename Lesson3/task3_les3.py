# В массиве случайных целых чисел поменять местами минимальный и максимальный
# элементы.

def gen_list(n, m, l):
    """Функция генерирует список заданной длинны l из случайных целых чисел в
    диапазоне от n до m."""
    from random import randint
    return [randint(n, m) for _ in range(l)]


my_list = gen_list(1, 200, 7)
print(my_list)
imin = imax = 0
my_max = my_min = my_list[0]
for i in range(len(my_list) - 1):
    if my_list[i + 1] > my_max:
        imax = i + 1
        my_max = my_list[i + 1]
    elif my_list[i + 1] < my_min:
        imin = i + 1
        my_min = my_list[i + 1]
my_list[imax], my_list[imin] = my_list[imin], my_list[imax]
print(my_list)
