# Матрицы смежности
# Граф описывается списком списков, где каждый вложенный список представляет
# собой описание вершины графаб а каждый элемент вложенного списка показывает
# наличие пути между вершинами(в соответствиис индексом элемента во
# вложенном списке) 0 - нет пути, 1 - есть путь (см. Graph1).

graph1 = [
    [0, 1, 1, 0],
    [1, 0, 1, 1],
    [1, 1, 0, 0],
    [0, 1, 0, 0]
]
print(*graph1, sep='\n')
print('*' * 50)
# В случае ориентированного графа(см. Graph2) матрица будет отображать наличие
# пути от вершины к вершинеб и будет выглядеть так (отсутствие симметрии относи
# тельно главной диагонали матрицы говорит о томб что данная матрица описывает
# ориентированый граф):

graph2 = [
    [0, 1, 1, 0],
    [0, 0, 1, 1],
    [0, 1, 0, 0],
    [0, 0, 0, 0]
]
print(*graph2, sep='\n')
print('*' * 50)

# Добавим на граф веса (см. Graph3) в этом случае мы заменим единицы на вес
# соответствующего ребра:

graph3 = [
    [0, 2, 3, 0],
    [0, 0, 2, 1],
    [0, 2, 0, 0],
    [0, 0, 0, 0]
]
print(*graph3, sep='\n')
print('*' * 50)

# При хранений графов в виде матрицы смежности мы будем тратить V**2 памяти,
# где V - количество вершин графа.

# Списки смежности:
# В отличии от матрицы, тут для каждой вершины создаются списки, в которых
# указываются вершины, с которой эта вершина связана рёбрами. Такой список
# занимает меньше памяти, но если мы захотим узнать, связана ли вершина 1 с
# вершиной 3, нам придется пройти до конца списка описывающего вершину 1,
# пока мы не найдем 3, либо не убедимся в ее отсутствии.

# рис. Graph1 вар1
graph = []
graph.append([1, 2])
graph.append([0, 2, 3])
graph.append([0, 1])
graph.append([1])

print(*graph3, sep='\n')
print('*' * 50)

# Для оптимизации целесообразно использовать в качестве хранения графа -
# словарь:

# рис. Graph1 вар2
graph = {
    0: {1, 2},
    1: {0, 2, 3},
    2: {0, 1},
    3: {1}
}

print(graph)

# В таком случае проверка наличия пути между вершинами 1 и 3 проводится
# мгновенно, без обхода списка:
if 3 in graph[1]:
    print(True)
print('*' * 50)

# В случае взвешенного графа, в описание добавляется пара значений - номер
# связаной вершины и вес соответствующего ребра:

# см. Graph4
from collections import namedtuple

Vertex = namedtuple('Vertex', ['vertex', 'edge'])

graph = []
graph.append([Vertex(1, 2), Vertex(2, 3)])
graph.append([Vertex(0, 2), Vertex(2, 2), Vertex(3, 1)])
graph.append([Vertex(0, 3), Vertex(1, 2)])
graph.append([Vertex(1, 1)])

print(*graph, sep='\n')
# проверка наличия пути между вершинами 1 и 3
for v in graph[1]:
    if v.vertex == 3:
        print(True)

print('*' * 50)


# Пример хранения графа в виде класса. Плюс данного способа заключается в том,
# что если нам нужно будет дополнить информацию о вершинахб то мы сможем её
# добавить в наш класс (например добавим переменную spam),  из минусов -
# придется прописывать доплнительные методы для вывода какой либро информации:
class Graph:
    def __init__(self, vertex, edge):
        self.vertex = vertex
        self.edge = edge


# class Graph:
#     def __init__(self, vertex, edge, spam):
#         self.vertex = vertex
#         self.edge = edge
#         self.spam = spam


# Третий способ хранения графов - список рёбер. Мы храним пару значений -
# название вершины, из которой ребро выходит, и название вершины куда оно
# заходит:

# см. Graph2

graph = [(0, 1), (0, 2), (1, 2), (1, 3), (2, 1)]
print(*graph, sep='\n')

# Это достаточно компактный способ представления графа, с точки зрения
# использования памяти.
print('*' * 50)
# В случае описания ориентированного графа с весами, логично будет добавить
# третий элемент (вес данного ребра):

# см. Graph3
graph = [(0, 1, 2), (0, 2, 3), (1, 2, 2), (1, 3, 1), (2, 1, 2)]
print(*graph, sep='\n')
