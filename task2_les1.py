# По введенным пользователем координатам двух точек вывести уравнение прямой
# вида y = kx + b, проходящей через эти точки.
x1 = float(input('Введите координату х первой точки: '))
y1 = float(input('Введите координату y первой точки: '))
x2 = float(input('Введите координату х второй точки: '))
y2 = float(input('Введите координату y второй точки: '))
if x1 == x2:
    print('Точки совпадают, невозможно построить прямую.'
          '' if y1 == y2 else f'Прямая параллельна оси Х. X = {x1}')
elif y1 == y2:
    print(f'Прямая параллельна оси Y. Y = {y1}')
else:
    k = (x2 - x1) / (y2 - y1)
    b = y1 - k * x1
    print(f'Уравнение прямой: Y = {k:.02f} * X + {b:.02f}'
          f'' if b >= 0 else f'Уравнение прямой: '
                             f'Y = {k:.02f} * X - {abs(b):.02f}')
