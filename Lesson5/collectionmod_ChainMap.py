# ChainMap (цепочка отображений) - позволяет организовать работу с несколькими
# словарями
# Поиск ключа осуществляется последовательно в каждом из словарей, пока ключ не
# будет найден
from collections import ChainMap


d_1 = {'a': 2, 'b': 4, 'c': 6}
d_2 = {'a': 10, 'b': 20, 'd': 40}
d_map = ChainMap(d_1, d_2)
print(d_map)
print('*' * 50)
d_2['a'] = 100
print(d_map)
print('*' * 50)
print(d_map['a']) # вернуло значение по первому найденному ключу 'a'
print(d_map['d'])

# добавим в коллекцию дополнительные словари в начале
print('*' * 50)
x = d_map.new_child({'a': 111, 'b': 222, 'c': 333, 'd': 444})
print(x)

# обращение непосредственно к одному из словарей
print('*' * 50)
print(x.maps[0])
print(x.maps[-1])

# узнать "родителей" коллекции
print('*' * 50)
print(x.parents)

print('*' * 50)
y = d_map.new_child()
print(y)
print(y['a'])
y['a'] = 1
print(y)
print(list(y))
print(list(y.values()))
print(list(y.maps[1]))
print(list(y.maps[1].values()))

print('*' * 50)

