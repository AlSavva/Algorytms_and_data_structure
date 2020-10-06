# В одномерном массиве найти сумму элементов, находящихся между минимальным и
# максимальным элементами. Сами минимальный и максимальный элементы в сумму не
# включать.

def gen_list(n, m, l):
    """Функция генерирует список заданной длинны l из случайных целых чисел в
    диапазоне от n до m."""
    from random import randint
    return [randint(n, m) for _ in range(l)]


my_list = gen_list(1, 15, 7)
print(my_list)
imin = imax = total = 0
my_max = my_min = my_list[0]
for i in range(len(my_list) - 1):
    if my_list[i + 1] > my_max:
        imax = i + 1
        my_max = my_list[i + 1]
    elif my_list[i + 1] < my_min:
        imin = i + 1
        my_min = my_list[i + 1]
if imin > imax:
    imin, imax = imax, imin
for i in range(imin + 1, imax):
    total += my_list[i]
print(f'Сумма элементов между минимальным и максимальным элементами: {total}')
