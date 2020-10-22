import hw_les6_ideal_two as id2

div2 = div3 = div5 = div7 = 0
for num in range(2, 100):
    if num % 2 == 0:
        div2 += 1
    if num % 3 == 0:
        div3 += 1
    if num % 5 == 0:
        div5 += 1
    if num % 7 == 0:
        div7 += 1
print(f'Кратно 2 - {div2}')
print(f'Кратно 3 - {div3}')
print(f'Кратно 4 - {div2 // 2}')
print(f'Кратно 5 - {div5}')
print(f'Кратно 6 - {div3 // 2}')
print(f'Кратно 7 - {div7}')
print(f'Кратно 8 - {div2 // 4}')
print(f'Кратно 9 - {div3 // 3}')

totmem = id2.SumMemory()
totmem.extend(div2, div3, div5, div7, num)
totmem.print_sum()

# Переменные заняли в сумме 140 байт(а)
# Переменные класса <class 'int'> в колличестве 5 заняли 140 байт(а).

a = [0] * 8
for num1 in range(2, 100):
    for i in range(2, 10):
        if num1 % i == 0:
            a[i - 2] += 1
num1 = 0
while num1 < len(a):
    print(f'Кратно {num1 + 2} - {a[num1]}')
    num1 += 1

totmem = id2.SumMemory()
totmem.extend(a, num1, i)
totmem.print_sum()

# Переменные заняли в сумме 400 байт(а)
# Переменные класса <class 'list'> в колличестве 1 заняли 120 байт(а).
# Переменные класса <class 'int'> в колличестве 10 заняли 280 байт(а).

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

totmem = id2.SumMemory()
totmem.extend(matrix, min_list, i, string)
totmem.print_sum()


# Переменные заняли в сумме 1676 байт(а)
# Переменные класса <class 'list'> в колличестве 7 заняли 808 байт(а).
# Переменные класса <class 'int'> в колличестве 31 заняли 868 байт(а).

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

totmem = id2.SumMemory()
totmem.extend(mymatr, a, check, mincol, i, j)
totmem.print_sum()

# Переменные заняли в сумме 1500 байт(а)
# Переменные класса <class 'list'> в колличестве 6 заняли 688 байт(а).
# Переменные класса <class 'int'> в колличестве 29 заняли 812 байт(а).

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

totmem = id2.SumMemory()
totmem.extend(M, N, a, i, b, j, mn, mx)
totmem.print_sum()

# Переменные заняли в сумме 1556 байт(а)
# Переменные класса <class 'int'> в колличестве 31 заняли 868 байт(а).
# Переменные класса <class 'list'> в колличестве 6 заняли 688 байт(а).
