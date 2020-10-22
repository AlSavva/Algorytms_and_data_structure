"""
    a. выбрать хорошую задачу, которую имеет смысл оценивать по памяти;
    b. написать 3 варианта кода (один у вас уже есть); проанализировать 3 варианта и выбрать оптимальный;
    c. результаты анализа (количество занятой памяти в вашей среде разработки) вставить в виде комментариев
в файл с кодом. Указать версию и разрядность вашей ОС и интерпретатора Python;
    d. написать общий вывод: какой из трёх вариантов лучше и почему.

    Задание les_3_task_6:
    В одномерном массиве найти сумму элементов, находящихся между минимальным и максимальным элементами.
Сами минимальный и максимальный элементы в сумму не включать.
"""
from random import randint
import sys


def show_info(solution):
    total_memo = 0

    def show_obj(obj, level=2):
        nonlocal total_memo
        print('\t' * level, f"type: {obj.__class__}, size: {sys.getsizeof(obj)}, object: {obj}")
        if hasattr(obj, "__iter__"):
            if hasattr(obj, "items"):
                for elem in obj.items():
                    show_obj(elem, level + 1)
            if not isinstance(obj, str):
                for elem in obj:
                    show_obj(elem, level + 1)
        total_memo += sys.getsizeof(obj)

    def wrapper(arr):
        nonlocal total_memo
        x = solution(arr)
        keys = list(x.keys())
        print(f"\tАнализ занятой памяти функцией: {solution.__name__}")
        for key in keys:
            show_obj(x[key])
        print(f"\tСуммарная занятая память функцией {solution.__name__}: {total_memo}")

    return wrapper


# Решение 1. Без встроенных функций.
@show_info
def solution_1(arr):
    pos_min, pos_max, ans = 0, 0, 0
    for i, elem in enumerate(arr):
        if elem < arr[pos_min]:
            pos_min = i
        elif elem > arr[pos_max]:
            pos_max = i
    for i in range(min(pos_min, pos_max) + 1, max(pos_min, pos_max)):
        ans += arr[i]
    print("\nРешение 1:")
    print(f"\tОтвет: сумма между минимальным числом ({arr[pos_min]}) и максимальным ({arr[pos_max]}): {ans}")
    return locals()


# Решение 2. Со встроенными функциями.
@show_info
def solution_2(arr):
    print("\nРешение 2:")
    print("\tОтвет: ",
          sum(arr[min(arr.index(min(arr)), arr.index(max(arr))) + 1:max(arr.index(min(arr)), arr.index(max(arr)))]))
    return locals()


# Решение 3. Используя рекурсию для поиска минимума и максимума.
@show_info
def solution_3(arr):
    mmr = {}
    i = 1

    def min_and_max(a, mn=float('inf'), mx=float('-inf')):
        nonlocal mmr, i
        if len(a) == 0:
            return mn, mx
        mn, mx = min(a[0], mn), max(a[0], mx)
        d = locals()
        for key, value in d.items():
            if key == 'min_and_max' or key == 'i' or key == 'mmr':
                continue
            else:
                mmr[key + str(i)] = value
        i += 1
        a.pop(0)

        return min_and_max(a[:], mn, mx)

    mini, maxi = min_and_max(arr[:])

    if arr.index(mini) < arr.index(maxi):
        first = arr.index(mini)
        second = arr.index(maxi)
    else:
        first = arr.index(maxi)
        second = arr.index(mini)
    print("\nРешение 3:")
    ans = sum(arr[first + 1: second])
    print(f"\tОтвет: {ans}")
    loc = locals()
    del loc['mmr']
    loc.update(mmr)
    return loc


def main(count):
    print(sys.version, sys.platform)
    arr = [randint(-100, 100) for _ in range(count)]
    print("\nСгенерированный массив:")
    print(f"\t{arr}")
    solution_1(arr)
    solution_2(arr)
    solution_3(arr)


main(5)

"""
Анализ решений:
    3.8.5 (tags/v3.8.5:580fbb0, Jul 20 2020, 15:43:08) [MSC v.1926 32 bit (Intel)] win32
    
    Суммарная занятая память функцией solution_1:   198
    Суммарная занятая память функцией solution_2:   130
    Суммарная занятая память функцией solution_3:   762
    
        2 вариант работает занимает меньше всего памяти, так как работает только с исходным массивом и
    не создает ни единой переменной, используя встроенные функции
        1 вариант занимает больше памяти чем второй, так как создает 5 дополнительных переменных типа int для хранения
    мин и макс числа, их индексов и ответа.
        3 вариант занимает в разы больше памяти, так как находит минимум и максимум в массиве рекурсивно. На каждом шаге
    рекурсия получает новый массив, содержащий на один элемент меньше. Таким образом, если в исходном массиве будет 10
    чисел, то рекурсия займет памяти для хранения 10 массивов. 
    
"""

# Результат работы программы:

# Сгенерированный массив:
# 	    [23, -40, -65, -96, -32]
#
# Решение 1:
# 	Ответ: сумма между минимальным числом (-96) и максимальным (23): -105
# 	Анализ занятой памяти функцией: solution_1
# 		 type: <class 'list'>, size: 60, object: [23, -40, -65, -96, -32]
# 			 type: <class 'int'>, size: 14, object: 23
# 			 type: <class 'int'>, size: 14, object: -40
# 			 type: <class 'int'>, size: 14, object: -65
# 			 type: <class 'int'>, size: 14, object: -96
# 			 type: <class 'int'>, size: 14, object: -32
# 		 type: <class 'int'>, size: 14, object: 3
# 		 type: <class 'int'>, size: 12, object: 0
# 		 type: <class 'int'>, size: 14, object: -105
# 		 type: <class 'int'>, size: 14, object: 2
# 		 type: <class 'int'>, size: 14, object: -32
# 	Суммарная занятая память функцией solution_1: 198
#
# Решение 2:
# 	Ответ:  -105
# 	Анализ занятой памяти функцией: solution_2
# 		 type: <class 'list'>, size: 60, object: [23, -40, -65, -96, -32]
# 			 type: <class 'int'>, size: 14, object: 23
# 			 type: <class 'int'>, size: 14, object: -40
# 			 type: <class 'int'>, size: 14, object: -65
# 			 type: <class 'int'>, size: 14, object: -96
# 			 type: <class 'int'>, size: 14, object: -32
# 	Суммарная занятая память функцией solution_2: 130
#
# Решение 3:
# 	Ответ: -105
# 	Анализ занятой памяти функцией: solution_3
# 		 type: <class 'list'>, size: 60, object: [23, -40, -65, -96, -32]
# 			 type: <class 'int'>, size: 14, object: 23
# 			 type: <class 'int'>, size: 14, object: -40
# 			 type: <class 'int'>, size: 14, object: -65
# 			 type: <class 'int'>, size: 14, object: -96
# 			 type: <class 'int'>, size: 14, object: -32
# 		 type: <class 'int'>, size: 14, object: -96
# 		 type: <class 'int'>, size: 14, object: 23
# 		 type: <class 'int'>, size: 12, object: 0
# 		 type: <class 'int'>, size: 14, object: 3
# 		 type: <class 'int'>, size: 14, object: -105
# 		 type: <class 'int'>, size: 14, object: 6
# 		 type: <class 'function'>, size: 68, object: <function solution_3.<locals>.min_and_max at 0x02EBB9B8>
# 		 type: <class 'list'>, size: 48, object: [-40, -65, -96, -32]
# 			 type: <class 'int'>, size: 14, object: -40
# 			 type: <class 'int'>, size: 14, object: -65
# 			 type: <class 'int'>, size: 14, object: -96
# 			 type: <class 'int'>, size: 14, object: -32
# 		 type: <class 'int'>, size: 14, object: 23
# 		 type: <class 'int'>, size: 14, object: 23
# 		 type: <class 'list'>, size: 44, object: [-65, -96, -32]
# 			 type: <class 'int'>, size: 14, object: -65
# 			 type: <class 'int'>, size: 14, object: -96
# 			 type: <class 'int'>, size: 14, object: -32
# 		 type: <class 'int'>, size: 14, object: -40
# 		 type: <class 'int'>, size: 14, object: 23
# 		 type: <class 'list'>, size: 40, object: [-96, -32]
# 			 type: <class 'int'>, size: 14, object: -96
# 			 type: <class 'int'>, size: 14, object: -32
# 		 type: <class 'int'>, size: 14, object: -65
# 		 type: <class 'int'>, size: 14, object: 23
# 		 type: <class 'list'>, size: 36, object: [-32]
# 			 type: <class 'int'>, size: 14, object: -32
# 		 type: <class 'int'>, size: 14, object: -96
# 		 type: <class 'int'>, size: 14, object: 23
# 		 type: <class 'list'>, size: 32, object: []
# 		 type: <class 'int'>, size: 14, object: -96
# 		 type: <class 'int'>, size: 14, object: 23
# 	Суммарная занятая память функцией solution_3: 762
#
