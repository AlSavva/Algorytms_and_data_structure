# Матрица 5x4 заполняется вводом с клавиатуры, кроме последних элементов
# строк. Программа должна вычислять сумму введенных элементов каждой строки и
# записывать ее в последнюю ячейку строки. В конце следует вывести полученную
# матрицу.

matrix = []
count = 1
while count < 5:
    row = []
    total = 0
    print(f'Заполняем ряд {count}')
    for i in range(4):
        num = int(input('Введите значение: '))
        row.append(num)
        total += num
    row.append(total)
    matrix.append(row)
    count += 1
print(f'Готово! Матрица сформирована: \n')
for line in matrix:
    for item in line:
        print(f'{item:>4}', end='')
    print()
