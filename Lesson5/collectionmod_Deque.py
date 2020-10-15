from collections import deque


# главноне отличие от списка в скорости доступа к элементам  О(1) для доступа
# к первому, либо последнему элементам
# О(n) к n - ному элементу
a = deque()
b = deque('abrakadabra')
c = deque([1, 2, 3, 4, 5])
print(a, b, c, sep='\n')
print('*' * 50)
b = deque('abrakadabra', maxlen=3) # регулирует длинну очереди, причем выпадают первые элементы
c = deque([1, 2, 3, 4, 5], maxlen=4)
print(b, c, sep='\n')
c.clear()
print(c)
print('*' * 50)
# Самые полезные св-ва это добавление элементов в начало или конец очереди
d = deque([i for i in range(5)])
print(d)
d.append(5)
d.appendleft(6)
print(d)
d.extend([17, 18, 19.5])
d.extendleft([False, (1, 2)]) # слева элементы добавляются в ОБРАТНОМ! порядке
print(d)
print('*' * 50)
# Для сравнения - как это будет работать, если ограничить длину очереди
d = deque([i for i in range(5)], maxlen=7)
print(d)
d.append(5)
d.appendleft(6)
print(d)
d.extend([17, 18, 19.5]) # из очереди "выйдут" 3 первых элемента
print(d)
d.extendleft([False, (1, 2)]) # из очереди "выйдут" 2 последних элемента
print(d)
# для удаления элементов из очереди используются pop и popleft
print('*' * 50)
f = deque([i for i in range(5)], maxlen=7)
print(f)
x = f.pop()
y = f.popleft()
print(f, x, y, sep='\n')
# некоторые методы очередей
print('*' * 50)
g = deque([i for i in range(5)], maxlen=7)
print(g)
print(f'g.count(2):\n{g.count(2)}')
print(f'g.index(3):\n{g.index(3)}')
g.insert(2, 6)
print(f'g.insert(2, 6):\n{g}')
g.reverse()
print(f'g.reverse():\n{g}')
g.rotate(3)
print(f'g.rotate(3):\n{g}')
g.rotate(-4)
print(f'g.rotate(-4):\n{g}')
# Применение на практике:
# Задача на разделение массива случайных чисел на положительные и отрицательные
print('*' * 50)
import random
lst =[random.randint(-100, 100) for _ in range(15)]
print(lst)
deq = deque()
for item in lst:
    if item > 0:
        deq.append(item)
    elif item < 0:
        deq.appendleft(item)
print(deq)
# Задача: существует файл big_log.txt в который постоянно добавляются IP - ад
# реса. Нам необходимо посмотреть только последние 10.
print('*' * 50)
with open('big_log.txt', 'r', encoding='utf-8') as infile:
    last_ten = deque(infile, 10)
print(last_ten)
