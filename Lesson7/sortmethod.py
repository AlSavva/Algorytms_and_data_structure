# Сортировка пузырьком(Bubblesort):
# Сложность О(n**2)
# Устойчивость (стабильность): Устойчивая(при наличии двух одинаковых элементов
# сохраняется их порядок).
# Тип (категория): обменная
# Потребление памяти: не требует доп. памяти

import random


def randarray(size):
    """
    Возвращает массив из size элементов от 0 до size - 1 в произвольном порядке
    """
    array = [i for i in range(size)]
    random.shuffle(array)
    return array


def full_randarray(x, y, size):
    """
    Возвращает массив из size элементов от x до y в произвольном порядке
    """
    array = [random.randint(x, y) for _ in range(size)]
    random.shuffle(array)
    return array


def bubsort(array):
    n = 1
    while n < len(array):
        for i in range(len(array) - n):
            if array[i] > array[i + 1]:
                array[i], array[i + 1] = array[i + 1], array[i]
        n += 1
    # return array здесь и далее, поскольку в качестве аргумента мы передаем
    # функции изменяемый объект(список) и выполняем действия внутри него, то
    # можно обойтись без return!


# Сортировка выбором(Selectionsort):
# Сложность: О(n**2) постоянная сложность!
# Устойчивость (стабильность): Устойчивая/неустойчивая(при наличии двух
# одинаковых элементов сохраняется их порядок) в примере реализован
# устойчивый вариант.
# Тип (категория): выбором
# Потребление памяти: не требует доп. памяти

def selectsort(array):
    for i in range(len(array)):
        idx_min = i
        for j in range(i + 1, len(array)):
            if array[j] < array[idx_min]:
                idx_min = j
        array[idx_min], array[i] = array[i], array[idx_min]


# Сортировка вставками(Insertionsort):
# Сложность: О(n**2) / O(n) лучшee время(когда массив уже отсортирован).
# Устойчивость (стабильность): Устойчивая(при наличии двух
# одинаковых элементов сохраняется их порядок).
# Тип (категория): вставками
# Потребление памяти: не требует доп. памяти

def insertsort(array):
    for i in range(1, len(array)):
        spam = array[i]
        j = i
        while array[j - 1] > spam and j > 0:
            array[j] = array[j - 1]
            j -= 1
        array[j] = spam


# Сортировка Шелла(Shellsort):
# Сложность: О(n**2) / O(n * (log n) ** 2) или О(n ** 3/2) лучшee время
# (зависит от шага).
# Устойчивость (стабильность): Неустойчивая(при наличии двух
# одинаковых элементов не сохраняется их порядок).
# Тип (категория): вставками
# Потребление памяти: не требует доп. памяти
# в рассматриваемом примере мы не будем делить значение приращения(шага) на 2,
# а используем ряд чисел, полученый эмпирическим путём: [1, 4, 10, 23, 57, 132,
# 301, 701, 1750] данная последовательность является лучшей при сортировке
# методом Шелла массивов длинной до 4000 элементов.

def shellsort(array):
    assert len(array) < 4000, 'Массив слишком большой!'

    def new_increment(array):
        inc = [1, 4, 10, 23, 57, 132, 301, 701, 1750]
        while len(array) <= inc[-1]:
            inc.pop()
        while len(inc) > 0:
            yield inc.pop()

    # count = 0
    for increment in new_increment(array):
        for i in range(increment, len(array)):
            for j in range(i, increment - 1, -increment):
                if array[j - increment] <= array[j]:
                    break
                array[j], array[j - increment] = array[j - increment], array[j]
    #             count += 1
    # print(count)


# Быстрая сортировка Хоара(quicksort):
# Сложность: О(n**2) / O(n * log n) лучшee время.
# Устойчивость (стабильность): Неустойчивая(при наличии двух
# одинаковых элементов сохраняется их порядок) Однако может быть доработана до
# устойчивой.
# Тип (категория): обменная
# Потребление памяти: O(n)/не требует доп. памяти (в примере - версия
# использующая доппамять)

def quicksort(array):
    if len(array) <= 1:
        return array
    pivot = random.choice(array)  # произвольно выбираем опорный элемент
    s_ar = []
    m_ar = []
    l_ar = []
    for item in array:
        if item < pivot:
            s_ar.append(item)
        elif item > pivot:
            l_ar.append(item)
        else:
            m_ar.append(item)
    return quicksort(s_ar) + m_ar + quicksort(l_ar)


# Версия без доппамяти:

def quicksort_no_memory(array, fst, lst):
    """
    Реализация сортировки Хоара без использования дополнительной памяти
    :param array: сортируемый массив
    :param fst: начало сортировки(индекс элемента)
    :param lst: конец сортировки(индекс элемента)
    :return: отсортированый массив от fst-ого до lst-того элемента.
    """
    if fst >= lst:
        return
    # print(array)
    pivot = array[random.randint(fst, lst)]
    i, j = fst, lst
    while i <= j:
        while array[i] < pivot:
            i += 1
        while array[j] > pivot:
            j -= 1
        if i <= j:
            array[i], array[j] = array[j], array[i]
            i, j = i + 1, j - 1
    quicksort_no_memory(array, fst, j)
    quicksort_no_memory(array, i, lst)


# Разворот массива,

def reverse(array):
    """
    Функция разворачивает массив в обратном порядке
    :param array: массив
    :return: массив в обратном порядке
    """
    for i in range(len(array) // 2):
        array[i], array[len(array) - 1 - i] = array[len(array) - 1 - i], array[
            i]


# Алгоритм сортировки Timesort(используется в функции sorted, и в методе sort):
# Сложность: O(n * log n) / О(n) лучшее время при отсортированном массиве.
# Устойчивость (стабильность): Устойчивая(при наличии двух
# одинаковых элементов сохраняется их порядок)
# Тип (категория): гибридная (Вставками + Слиянием)
# Потребление памяти: O(n)

# Python3 program to perform basic timSort
MIN_MERGE = 32


def calcMinRun(n):
    """Returns the minimum length of a
    run from 23 - 64 so that
    the len(array)/minrun is less than or
    equal to a power of 2.

    e.g. 1=>1, ..., 63=>63, 64=>32, 65=>33,
    ..., 127=>64, 128=>32, ...
    """
    r = 0
    while n >= MIN_MERGE:
        r |= n & 1
        n >>= 1
    return n + r


# This function sorts array from left index to
# to right index which is of size atmost RUN
def insertionSort(arr, left, right):
    for i in range(left + 1, right + 1):
        j = i
        while j > left and arr[j] < arr[j - 1]:
            arr[j], arr[j - 1] = arr[j - 1], arr[j]
            j -= 1


# Merge function merges the sorted runs
def merge(arr, l, m, r):
    # original array is broken in two parts
    # left and right array
    len1, len2 = m - l + 1, r - m
    left, right = [], []
    for i in range(0, len1):
        left.append(arr[l + i])
    for i in range(0, len2):
        right.append(arr[m + 1 + i])

    i, j, k = 0, 0, l

    # after comparing, we merge those two array
    # in larger sub array
    while i < len1 and j < len2:
        if left[i] <= right[j]:
            arr[k] = left[i]
            i += 1

        else:
            arr[k] = right[j]
            j += 1

        k += 1

    # Copy remaining elements of left, if any
    while i < len1:
        arr[k] = left[i]
        k += 1
        i += 1

    # Copy remaining element of right, if any
    while j < len2:
        arr[k] = right[j]
        k += 1
        j += 1


# Iterative Timsort function to sort the
# array[0...n-1] (similar to merge sort)
def timSort(arr):
    n = len(arr)
    minRun = calcMinRun(n)

    # Sort individual subarrays of size RUN
    for start in range(0, n, minRun):
        end = min(start + minRun - 1, n - 1)
        insertionSort(arr, start, end)

        # Start merging from size RUN (or 32). It will merge
    # to form size 64, then 128, 256 and so on ....
    size = minRun
    while size < n:

        # Pick starting point of left sub array. We
        # are going to merge arr[left..left+size-1]
        # and arr[left+size, left+2*size-1]
        # After every merge, we increase left by 2*size
        for left in range(0, n, 2 * size):
            # Find ending point of left sub array
            # mid+1 is starting point of right sub array
            mid = min(n - 1, left + size - 1)
            right = min((left + 2 * size - 1), (n - 1))

            # Merge sub array arr[left.....mid] &
            # arr[mid+1....right]
            merge(arr, left, mid, right)

        size = 2 * size


# Сортировка слиянием(Mergesort):
# Сложность: O(n * log n) среднее время.
# Тип: Слиянием
# Потребление памяти: O(n)

def merge1(left_list, right_list):
    sorted_list = []
    left_list_index = right_list_index = 0

    # Длина списков часто используется, поэтому создадим переменные для удобства
    left_list_length, right_list_length = len(left_list), len(right_list)

    for _ in range(left_list_length + right_list_length):
        if left_list_index < left_list_length and right_list_index < right_list_length:
            # Сравниваем первые элементы в начале каждого списка
            # Если первый элемент левого подсписка меньше, добавляем его
            # в отсортированный массив
            if left_list[left_list_index] <= right_list[right_list_index]:
                sorted_list.append(left_list[left_list_index])
                left_list_index += 1
            # Если первый элемент правого подсписка меньше, добавляем его
            # в отсортированный массив
            else:
                sorted_list.append(right_list[right_list_index])
                right_list_index += 1

        # Если достигнут конец левого списка, элементы правого списка
        # добавляем в конец результирующего списка
        elif left_list_index == left_list_length:
            sorted_list.append(right_list[right_list_index])
            right_list_index += 1
        # Если достигнут конец правого списка, элементы левого списка
        # добавляем в отсортированный массив
        elif right_list_index == right_list_length:
            sorted_list.append(left_list[left_list_index])
            left_list_index += 1

    return sorted_list


def merge_sort(nums):
    # Возвращаем список, если он состоит из одного элемента
    if len(nums) <= 1:
        return nums

    # Для того чтобы найти середину списка, используем деление без остатка
    # Индексы должны быть integer
    mid = len(nums) // 2

    # Сортируем и объединяем подсписки
    left_list = merge_sort(nums[:mid])
    right_list = merge_sort(nums[mid:])

    # Объединяем отсортированные списки в результирующий
    return merge1(left_list, right_list)


# Сортировка сложных структур с использованием ключа(пример):
# Создадим несколько персонажей, и отсортируем их(например по имени)
from collections import namedtuple

Person = namedtuple('Person', 'name, age')
p_1 = Person('Vasya', 25)
p_2 = Person('Kolya', 30)
p_3 = Person('Olya', 23)
p_4 = Person('Ivan', 60)
p_5 = Person('Ira', 44)
people = [p_1, p_2, p_3, p_4, p_5]
print(people)
print('*' * 50)
result = sorted(people)  # сортируем при помощи встроенной функции. Получим
# сортировку по именам
print(result)
print('*' * 50)
# result1 = sorted(people, key=age)  # теперь отсортируем при помощи встроенной
# функции, используя сортировку по ключу 'age' - Получим ошибку - переменная
# age не определена.
# print(result1)
print('*' * 50)


def by_age(person):  # можно написать отдельную функцию, которая возвращает
    # возраст
    return person.age


result2 = sorted(people, key=by_age)
print(result2)
print('*' * 50)
result3 = sorted(people,
                 key=lambda x: x.age)  # либо использовать лямбда-функцию
print(result3)
print('*' * 50)

# также можно использовать функцию attrgetter из модуля operator
from operator import attrgetter

result4 = sorted(people, key=attrgetter('age'))
print(result4)

# a = full_randarray(0, 10, 10)
# print(a)
# timSort(a)
# print(a)

# b = randarray(15)
# print(b)
# selectsort(b)
# print(b)
# c = randarray(20)
# print(c)
# bubsort(c)
# print(c)
