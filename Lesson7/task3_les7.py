# 3. Массив размером 2m + 1, где m — натуральное число, заполнен случайным
# образом. Найдите в массиве медиану. Медианой называется элемент ряда, делящий
# его на две равные части: в одной находятся элементы, которые не меньше
# медианы, в другой — не больше медианы.
# Примечание: задачу можно решить без сортировки исходного массива. Но если это
# слишком сложно, используйте метод сортировки, который не рассматривался на
# уроках (сортировка слиянием также недопустима).

import random


def full_randarray(x, y, size):
    """
    Возвращает массив из size элементов от x до y в произвольном порядке
    """
    array = [random.randint(x, y) for _ in range(size)]
    random.shuffle(array)
    return array

def median_search(array):
    if len(array) == 1:
        return array[0]
    else:
        array.remove(max(array))
        array.remove(min(array))
        return median_search(array)
b = full_randarray(0, 9, 9)
print(b)
print(median_search(b))
