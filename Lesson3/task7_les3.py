# В одномерном массиве целых чисел определить два наименьших элемента. Они
# могут быть как равны между собой (оба минимальны), так и различаться.

def gen_list(n, m, l):
    """Функция генерирует список заданной длинны l из случайных целых чисел в
    диапазоне от n до m."""
    from random import randint
    return [randint(n, m) for _ in range(l)]


my_list = gen_list(-1, 10, 10)
print(my_list)
imin1 = 0
imin2 = 1
if my_list[imin1] > my_list[imin2]:
    imin1, imin2 = imin2, imin1
for i in range(3, len(my_list)):
    if my_list[i] < my_list[imin1]:
        if my_list[imin1] < my_list[imin2]:
            imin2 = imin1
        imin1 = i
    elif my_list[i] < my_list[imin2]:
        imin2 = i
print(f'Минимальные элементы массива: {my_list[imin1]} и {my_list[imin2]}')
