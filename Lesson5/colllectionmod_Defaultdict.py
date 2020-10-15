# объект максимально похожий на словарь, с теми же методами
# что и у обычного словаря. Но в отличии от словаря, при создании ему необхо
# димо передать какую либо функцию.
from collections import defaultdict


a = defaultdict()
print(a)

s = 'qwertyuioasdfghjkzxcvbnmlkjhgfdsiuytre'
b =defaultdict(int)
for i in s:
    b[i] += 1 # не прокатит с обычным словарем, т.к. изначально ключи отсутствуют в словаре
print(b)   # но в данном случае, переданная функция int генерирует у отсутствующего ключа значение 0
print('*' * 50)

lst_1 = [('cat', 1), ('dog', 5), ('cat', 2), ('mouse', 1), ('dog', 1)]
c = defaultdict(list)
for k, v in lst_1:
    c[k].append(v)
print(c)
print('*' * 50)

lst_2 = [('cat', 1), ('dog', 5), ('cat', 2),('cat', 1) ,('mouse', 1),
         ('dog', 1), ('dog', 5)]
d = defaultdict(set)
for k, v in lst_1:
    d[k].add(v)
print(d)
#  в качестве функций можно передавать собственные, и лямбда функции
print('*' * 50)

f = defaultdict(lambda: 'unknown')
f.update(rex='dog', thomas='cat', jerry='mouse')
print(f)
print(f['rex'])
print(f['barsik'])
print(f) # f['barsik'] не только вывело значение по отсутсвующему ключу но и добавило в словарь
