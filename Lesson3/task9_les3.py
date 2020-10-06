# Найти максимальный элемент среди минимальных элементов столбцов матрицы.

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


mymatr = my_matrix(6, 8)
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
