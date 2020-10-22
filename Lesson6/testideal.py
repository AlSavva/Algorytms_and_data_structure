from hw_les6_ideal import var_memory
# div2 = div3 = div5 = div7 = 0
# for num in range(2, 100):
#     if num % 2 == 0:
#         div2 += 1
#     if num % 3 == 0:
#         div3 += 1
#     if num % 5 == 0:
#         div5 += 1
#     if num % 7 == 0:
#         div7 += 1
# print(f'Кратно 2 - {div2}')
# print(f'Кратно 3 - {div3}')
# print(f'Кратно 4 - {div2 // 2}')
# print(f'Кратно 5 - {div5}')
# print(f'Кратно 6 - {div3 // 2}')
# print(f'Кратно 7 - {div7}')
# print(f'Кратно 8 - {div2 // 4}')
# print(f'Кратно 9 - {div3 // 3}')
# # Переменная= div2;	Тип= <class 'int'>;	Значение= 49;	Занимает 28 байт(а).
# # Переменная= div3;	Тип= <class 'int'>;	Значение= 33;	Занимает 28 байт(а).
# # Переменная= div5;	Тип= <class 'int'>;	Значение= 19;	Занимает 28 байт(а).
# # Переменная= div7;	Тип= <class 'int'>;	Значение= 14;	Занимает 28 байт(а).
# # Переменная= num;	Тип= <class 'int'>;	Значение= 99;	Занимает 28 байт(а).
# # Все переменные заняли 140 байт(а).
#
# a = [0] * 8
# for num1 in range(2, 100):
#     for i in range(2, 10):
#         if num1 % i == 0:
#             a[i - 2] += 1
# num1 = 0
# while num1 < len(a):
#     print(f'Кратно {num1 + 2} - {a[num1]}')
#     num1 += 1
# # Переменная= a;	Тип= <class 'list'>;	Значение= [49, 33, 24, 19, 16, 14, 12, 11];	Занимает 120 байт(а).
# # Переменная= num1;	Тип= <class 'int'>;	Значение= 8;	Занимает 28 байт(а).
# # Переменная= i;	Тип= <class 'int'>;	Значение= 9;	Занимает 28 байт(а).
# # Все переменные заняли 176 байт(а).

import random

#
# matrix = []
#
# for i in range(4):
#     matrix.append([])
#     matrix[i].extend([random.randint(1, 10) for _ in range(5)])
#
# min_list = []
# min_list.extend(matrix[0])
#
# for string in matrix:
#     print()
#     print(('{:4d} ' * len(string)).format(*string))
#     i = 0
#     for j in string:
#         if j < min_list[i]:
#             min_list[i] = j
#         i += 1
#
# print()
# print('min_list')
# print(('{:4d} ' * len(min_list)).format(*min_list))
# print()
#
# min_list.sort(reverse=True)
# print(
#     'Максимальный элемент среди минимальных элементов столбцов матрицы: ',
#     min_list[0]
# )


# Переменная= matrix;	Тип= <class 'list'>;	Значение= [[8, 10, 9, 9, 5], [2, 7, 2, 9, 9], [5, 9, 2, 1, 4], [10, 2, 1, 9, 7]];	Занимает 88 байт(а).
# Переменная= i;	Тип= <class 'int'>;	Значение= 5;	Занимает 28 байт(а).
# Переменная= min_list;	Тип= <class 'list'>;	Значение= [2, 2, 1, 1, 4];	Занимает 120 байт(а).
# Переменная= string;	Тип= <class 'list'>;	Значение= [10, 2, 1, 9, 7];	Занимает 120 байт(а).
# Переменная= j;	Тип= <class 'int'>;	Значение= 7;	Занимает 28 байт(а).
# Все переменные заняли 384 байт(а).

# def my_matrix(rows, cols):
#     """Функция генерирует матрицу размером row x col из произвольных чисел от
#     1 до 10"""
#     from random import randint
#     matrix = [[randint(1, 10) for _ in range(cols)] for _ in range(rows)]
#     for line in matrix:
#         for item in line:
#             print(f'{item:>4}', end='')
#         print()
#     return matrix
#
#
# mymatr = my_matrix(4, 5)
# a = []
# check = -1
# for i in range(len(mymatr[0])):
#     mincol = mymatr[0][i]
#     for j in range(len(mymatr) - 1):
#         if mymatr[j + 1][i] < mincol:
#             mincol = mymatr[j + 1][i]
#     a.append(mincol)  # необязательно. чисто для наглядности.
#     if check == -1:
#         check = mincol
#     elif check < mincol:
#         check = mincol
# print(f'Минимальные значения столбцов матрицы: \n\t{a}')
# print(f'Максимальный элемент среди минимальных значений столбцов матрицы: '
#       f'{check}')

# Переменная= mymatr;	Тип= <class 'list'>;	Значение= [[4, 5, 2, 2, 10], [10, 5, 2, 2, 4], [4, 1, 3, 7, 6], [10, 1, 7, 2, 3]];	Занимает 88 байт(а).
# Переменная= a;	Тип= <class 'list'>;	Значение= [4, 1, 2, 2, 3];	Занимает 120 байт(а).
# Переменная= check;	Тип= <class 'int'>;	Значение= 4;	Занимает 28 байт(а).
# Переменная= i;	Тип= <class 'int'>;	Значение= 4;	Занимает 28 байт(а).
# Переменная= mincol;	Тип= <class 'int'>;	Значение= 3;	Занимает 28 байт(а).
# Переменная= j;	Тип= <class 'int'>;	Значение= 2;	Занимает 28 байт(а).
# Все переменные заняли 320 байт(а).

# M = 5
# N = 4
# a = []
# for i in range(N):
#     b = []
#     for j in range(M):
#         n = int(random.randint(1, 10))
#         b.append(n)
#         print('%4d' % n, end='')
#     a.append(b)
#     print()
#
# mx = -1
# for j in range(M):
#     mn = 200
#     for i in range(N):
#         if a[i][j] < mn:
#             mn = a[i][j]
#     if mn > mx:
#         mx = mn
# print("Максимальный среди минимальных: ", mx)

# Переменная= M;	Тип= <class 'int'>;	Значение= 5;	Занимает 28 байт(а).
# Переменная= N;	Тип= <class 'int'>;	Значение= 4;	Занимает 28 байт(а).
# Переменная= a;	Тип= <class 'list'>;	Значение= [[10, 4, 10, 5, 3], [8, 9, 5, 1, 1], [10, 9, 9, 10, 3], [10, 7, 10, 1, 5]];	Занимает 88 байт(а).
# Переменная= i;	Тип= <class 'int'>;	Значение= 3;	Занимает 28 байт(а).
# Переменная= b;	Тип= <class 'list'>;	Значение= [10, 7, 10, 1, 5];	Занимает 120 байт(а).
# Переменная= j;	Тип= <class 'int'>;	Значение= 4;	Занимает 28 байт(а).
# Переменная= n;	Тип= <class 'int'>;	Значение= 5;	Занимает 28 байт(а).
# Переменная= mx;	Тип= <class 'int'>;	Значение= 8;	Занимает 28 байт(а).
# Переменная= mn;	Тип= <class 'int'>;	Значение= 1;	Занимает 28 байт(а).
# Все переменные заняли 404 байт(а).


print(var_memory(locals(), verbose=True))
