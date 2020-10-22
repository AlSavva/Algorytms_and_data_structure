import sys

print(sys.version, sys.platform)


# 3.8.3 (default, Jul  2 2020, 17:30:36) [MSC v.1916 64 bit (AMD64)] win32

def show_size(x, level=0):
    """функция, показывает размер объекта, а так же размер
вложенных объектов, на которые он ссылается"""
    if hasattr(x, '__iter__'):
        if hasattr(x, 'items'):
            for xx in x.items():
                show_size(xx, level + 1)
        elif not isinstance(x, str):
            for xx in x:
                show_size(xx, level + 1)
    print('\t' * level,
          f'type= {x.__class__}, size= {sys.getsizeof(x)}'
          f', object= {x}')


def tot_size(x, tot=0):
    """Функция возвращает суммарный размер объекта,
    с учётом вложенных объектов"""
    tot += sys.getsizeof(x)
    if hasattr(x, '__iter__'):
        if hasattr(x, 'items'):
            for xx in x.items():
                tot += tot_size(xx, tot=0)
        elif not isinstance(x, str):
            for xx in x:
                tot += tot_size(xx, tot=0)
    return tot


# Найти максимальный элемент среди минимальных элементов столбцов матрицы.
# Вариант 1
import random

matrix = []

for i in range(4):
    matrix.append([])
    matrix[i].extend([random.randint(1, 10) for _ in range(5)])

min_list = []
min_list.extend(matrix[0])

for string in matrix:
    print()
    print(('{:4d} ' * len(string)).format(*string))
    i = 0
    for j in string:
        if j < min_list[i]:
            min_list[i] = j
        i += 1

print()
print('min_list')
print(('{:4d} ' * len(min_list)).format(*min_list))
print()

min_list.sort(reverse=True)
print(
    'Максимальный элемент среди минимальных элементов столбцов матрицы: ',
    min_list[0]
)
for el in (matrix, min_list, i, string):
    print(el.__class__, tot_size(el))
print(sum(tot_size(el) for el in (matrix, min_list, i, string)))


# <class 'list'> 1128
# <class 'list'> 260
# <class 'int'> 28
# <class 'list'> 260
# выделено 1676 байт памяти под переменные


# Вариант2:
def my_matrix(rows, cols):
    """Функция генерирует матрицу размером row x col из произвольных чисел от
    1 до 10"""
    from random import randint
    matrix = [[randint(1, 10) for _ in range(cols)] for _ in range(rows)]
    for line in matrix:
        for item in line:
            print(f'{item:>4}', end='')
        print()
    return matrix


mymatr = my_matrix(4, 5)
a = []
check = -1
for i in range(len(mymatr[0])):
    mincol = mymatr[0][i]
    for j in range(len(mymatr) - 1):
        if mymatr[j + 1][i] < mincol:
            mincol = mymatr[j + 1][i]
    a.append(mincol)  # необязательно. чисто для наглядности.
    if check == -1:
        check = mincol
    elif check < mincol:
        check = mincol
print(f'Минимальные значения столбцов матрицы: \n\t{a}')
print(f'Максимальный элемент среди минимальных значений столбцов матрицы: '
      f'{check}')
for el in (mymatr, a, check, mincol, i, j):
    print(el.__class__, tot_size(el))
print(sum(tot_size(el) for el in (mymatr, a, check, mincol, i, j)))
# <class 'list'> 1128
# <class 'list'> 260
# <class 'int'> 28
# <class 'int'> 28
# <class 'int'> 28
# <class 'int'> 28
# выделено 1500 байт памяти под переменные

# Вариант3:
from random import randint

M = 5
N = 4
a = []
for i in range(N):
    b = []
    for j in range(M):
        n = int(random.randint(1, 10))
        b.append(n)
        print('%4d' % n, end='')
    a.append(b)
    print()

mx = -1
for j in range(M):
    mn = 200
    for i in range(N):
        if a[i][j] < mn:
            mn = a[i][j]
    if mn > mx:
        mx = mn
print("Максимальный среди минимальных: ", mx)
for el in (M, N, a, i, b, j, mn, mx):
    print(el.__class__, tot_size(el))
print(sum(tot_size(el) for el in (M, N, a, i, b, j, mn, mx)))
# <class 'int'> 28
# <class 'int'> 28
# <class 'list'> 1128
# <class 'int'> 28
# <class 'list'> 260
# <class 'int'> 28
# <class 'int'> 28
# <class 'int'> 28
# выделено 1556 байт памяти под переменные

# Вывод - по использованию памяти под переменные лучше использовать вариант 2.