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
# В диапазоне натуральных чисел от 2 до 99 определить, сколько из них кратны
# каждому из чисел в диапазоне от 2 до 9. Примечание: 8 разных ответов.
# Вариант1:
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
for el in (div2, div3, div5, div7, num):
    print(el.__class__, tot_size(el))
print(sum(tot_size(el) for el in (div2, div3, div5, div7, num)))
# <class 'int'> 28
# <class 'int'> 28
# <class 'int'> 28
# <class 'int'> 28
# <class 'int'> 28
# 140
# выделено 140 байт памяти под переменные
# Вариант2:
a = [0] * 8
for num1 in range(2, 100):
    for i in range(2, 10):
        if num1 % i == 0:
            a[i - 2] += 1
num1 = 0
while num1 < len(a):
    print(f'Кратно {num1 + 2} - {a[num1]}')
    num1 += 1
for el in (a, num1, i):
    print(el.__class__, tot_size(el))
print(sum(tot_size(el) for el in (a, num1, i)))
# <class 'list'> 344
# <class 'int'> 28
# <class 'int'> 28
# 400
# выделено 400 байт памяти под переменные
