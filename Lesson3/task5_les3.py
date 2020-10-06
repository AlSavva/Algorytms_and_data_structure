# В массиве найти максимальный отрицательный элемент. Вывести на экран его
# значение и позицию в массиве.
# Примечание к задаче: пожалуйста не путайте «минимальный» и «максимальный
# отрицательный». Это два абсолютно разных значения.

def gen_list(n, m, l):
    """Функция генерирует список заданной длинны l из случайных целых чисел в
    диапазоне от n до m."""
    from random import randint
    return [randint(n, m) for _ in range(l)]


my_list = gen_list(-100, 100, 15)
print(my_list)
imax = -1
for i in range(len(my_list)):
    if my_list[i] < 0 and imax == -1:
        imax = i
    elif my_list[i] < 0 and imax != -1:
        if my_list[i] > my_list[imax]:
            imax = i
print(f'Максимальный отрицательный элемент массива {my_list[imax]} '
      f'индекс элемента - {imax}')
