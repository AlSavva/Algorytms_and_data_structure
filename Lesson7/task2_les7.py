# 2. Отсортируйте по возрастанию методом слияния одномерный вещественный
# массив, заданный случайными числами на промежутке [0; 50). Выведите на экран
# исходный и отсортированный массивы.
import random


def full_randarray(x, y, size):
    """
    Возвращает массив из size элементов от x до y(исключительно) в произвольном
    порядке
    """
    array = [random.uniform(x, y - 1) for _ in range(size)]
    random.shuffle(array)
    return array


def merge_sort(array):
    def merge(leftlst, rightlst):
        sortedlst = []
        leftlstidx = rightlstidx = 0
        leftlstlen, rightlstlen = len(leftlst), len(rightlst)
        for _ in range(leftlstlen + rightlstlen):
            if leftlstidx < leftlstlen and rightlstidx < rightlstlen:
                # Сравниваем первые элементы в начале каждого списка
                # Если первый элемент левого подсписка меньше, добавляем его
                # в отсортированный массив
                if leftlst[leftlstidx] <= rightlst[rightlstidx]:
                    sortedlst.append(leftlst[leftlstidx])
                    leftlstidx += 1
                # Если первый элемент правого подсписка меньше, добавляем его
                # в отсортированный массив
                else:
                    sortedlst.append(rightlst[rightlstidx])
                    rightlstidx += 1
            # Если достигнут конец левого списка, элементы правого списка
            # добавляем в конец результирующего списка
            elif leftlstidx == leftlstlen:
                sortedlst.append(rightlst[rightlstidx])
                rightlstidx += 1
            # Если достигнут конец правого списка, элементы левого списка
            # добавляем в отсортированный массив
            elif rightlstidx == rightlstlen:
                sortedlst.append(leftlst[leftlstidx])
                leftlstidx += 1
        return sortedlst

    # рекурсия для подсписков
    # Возвращаем список, если он состоит из одного элемента
    if len(array) <= 1:
        return array
    # Для того чтобы найти середину списка, используем деление без остатка
    mid = len(array) // 2
    # Сортируем и объединяем подсписки
    left_list = merge_sort(array[:mid])
    right_list = merge_sort(array[mid:])
    # Объединяем отсортированные списки в результирующий
    return merge(left_list, right_list)


a = full_randarray(0, 50, 20)
print(f'Исходный список: {a}')
print(f'Результат: {merge_sort(a)}')
