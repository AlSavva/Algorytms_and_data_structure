# OrderDict - упорядоченный словарьб который запоминает порядокб в которм были
# добавлены ключи.
from collections import OrderedDict

a = {'cat': 5, 'dog': 2, 'mouse': 4}
new_a = OrderedDict(sorted(a.items(), key=lambda x: x[0]))
print(new_a)
print('*' * 50)

b = {'cat': 5, 'mouse': 4, 'dog': 2}
new_b = OrderedDict(sorted(b.items(), key=lambda x: x[1]))
print(new_b)
print('*' * 50)
# можно поменять порядок объектов в упорядоченном словаре
new_b.move_to_end('mouse')  # переносит в конец списка
print(new_b)
new_b.move_to_end('mouse', last=False)  # переносит в начало списка
print(new_b)
print('*' * 50)

# для удаления элемента используют метод .popitem() - удаляет элемент из конца
# словаря. если передать дополнительно last=False - удалит первый элемент
new_b.popitem()
print(new_b)
new_b['cow'] = 3  # новый ключ добавляется в конец
print(new_b)
new_b.popitem(last=False)
print(new_b)
print('*' * 50)

# если мы изменим значение у существующего ключаб значение изменитсяб а порядок
# элементов останется прежним
new_b['dog'] = 8
print(new_b)
print('*' * 50)

# можно сортировать по разным параметрам, например по длине ключа
new_c = OrderedDict(sorted(a.items(), key=lambda x: len(x[0])))
print(new_c)
print('*' * 50)

# можно выводить элементы в обратном порядке
for key in reversed(new_c):
    print(key, new_c[key])
print('*' * 50)

#  в лог файл сохраняются ip адреса, с которых пришел запрос
# проанализировать последние N адресов, и сохранить в новый файл пары значений
# адрес - количество запросов
# исключить локальные адреса: 192.168.*.*
# сохранить исходный порядок адресов4
from collections import defaultdict, deque

N = 3000
with open('big_log.txt', 'r', encoding='utf-8') as infile:
    log = deque(infile, N)
data = OrderedDict()
spam = defaultdict(int)
for item in log:
    ip = item[:-1]
    if not ip.startswith('192.168'):
        spam[ip] += 1  # считает количество запросов с адреса
        data[ip] = 1  # сохраняет порядок адресов
# print(spam)
# print(data)
data.update(
    spam)  # в словарь data добавляем ключи из словаря спам(при изменении значения - позиция в OrderedDict не изменится)
# print(data)
with open('data.txt', 'w', encoding='utf-8') as outfile:
    for key, value in data.items():
        outfile.write(f'{key} - {value}\n')
