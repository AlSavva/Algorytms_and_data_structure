import sys
import ctypes
import struct

print(sys.version, sys.platform)

# в зависимости от разрядности системы, объекты занимают разное место в памяти
# в 32-х битной меньше, в 64-х битной больше.

a = 5
x = y = a
b = 125.54
c = 'Hello World!'

# print(sys.getsizeof(a))  # возвращает объем занимаемой памяти в байтах
# print(sys.getsizeof(b))
# print(sys.getsizeof(c))
#
lst = [i for i in range(10)]
print(sys.getsizeof(lst))


# создадим функцию, которая показывает размер объектов, и тех
# объектов, на которые он ссылается
def show_size(x, level=0):
    print('\t' * level, f'type= {x.__class__}, size= {sys.getsizeof(x)}'
                         f', object= {x}')
    # если у переданного объекта х есть атрибут
    # 'iter' то будем выводить информацию об объектах, хранящихся в нём.
    if hasattr(x, '__iter__'):
        # так же учтем, что передаваемый объект может быть словарем
        if hasattr(x, 'items'):
            for xx in x.items():
                show_size(xx, level + 1)
        # проверим, не является переданый объект строкой, чтобы избежать
        # переполнения стека
        elif not isinstance(x, str):
            for xx in x:
                show_size(xx, level + 1)
show_size(a)
show_size(b)
show_size(c)
show_size(lst)
print('*' * 50)
tup = tuple(lst)
show_size(tup)
print('*' * 50)
st = set(lst)
show_size(st)
print('*' * 50)
dct = {str(i): i for i in range(10)}
show_size(dct)

# print(id(a)) # возвращает адрес объекта в памяти
# print(sys.getsizeof(a))
# print(ctypes.string_at(id(a), sys.getsizeof(a)))
# print(struct.unpack('LLLLLLl', ctypes.string_at(id(a), sys.getsizeof(a))))
# print(id(int))
# print('*' * 50)
# print(id(b))
# print(sys.getsizeof(b))
# print(ctypes.string_at(id(b), sys.getsizeof(b)))
# print(struct.unpack('LLLd', ctypes.string_at(id(b), sys.getsizeof(b))))
# print(id(float))
# z = b
# b = 122.99
# print(struct.unpack('LLLd', ctypes.string_at(id(b), sys.getsizeof(b))))
# print('*' * 50)
# print(id(c))
# print(sys.getsizeof(c))
# print(ctypes.string_at(id(c), sys.getsizeof(c)))
# print(struct.unpack('LLLLLLLLLLli' + 'c' * 13, ctypes.string_at(id(c), sys.getsizeof(c))))
# print(id(str))
# print('*' * 50)
# d = [1,2,3,4]
# print(id(d))
# print(sys.getsizeof(d))
# print(ctypes.string_at(id(d), sys.getsizeof(d)))
# print(struct.unpack('LLLL' + 'LL' * 3 * 3, ctypes.string_at(id(d), sys.getsizeof(d))))
# print(id(list))
