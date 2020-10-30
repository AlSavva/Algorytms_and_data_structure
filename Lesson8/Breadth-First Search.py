# Поиск в ширину работает путем последовательного просмотра отдельных уровней
# графа, начиная с узла источника:
# Алгоритм поиска:
# 1. Поместить вершину, с которой начинаем поиск в пустую очередь.
# 2. Извлечь из начала очереди вершину.
#   а. Если вершина является целевой - завершить поиск.
#   б. В противном случае, в конец очереди помещаются все смежные вершины,
#   которые еще не пройдены, и не находятся в очереди.
# 3. Если очередь пуста - то все вершины графа были просмотрены, следовательно,
# целевая вершина недостижима из начальной. Завершить поиск.

# В качестве примера будет рассмотрен граф изображённый на рис. Graph5
# Следует запомнить,  что поиск в ширину является оптимальным для НЕВЗВЕШЕННЫХ
# графов, он находит минимальное количество шагов - ребер между начальной и
# целевой вершинами, без учета их стоимости - веса.
from collections import deque

# Матрица смежности:
graph = [
    [0, 1, 1, 0, 1, 0, 0, 0],
    [1, 0, 0, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 0, 0, 1, 0, 0],
    [1, 0, 1, 0, 0, 0, 1, 0],
    [0, 0, 0, 1, 0, 0, 1, 1],
    [0, 0, 0, 0, 1, 1, 0, 1],
    [0, 0, 0, 0, 0, 1, 1, 0]
]


def bfc(graph, start, finish):
    """
    :param graph: graph matrix
    :param start: start vertex
    :param finish: target vertex
    :return: short cut from start to finish
    """
    parent = [None for _ in range(len(graph))]
    is_visited = [False for _ in range(len(graph))]
    deq = deque([start])
    is_visited[start] = True
    while len(deq) > 0:
        curent = deq.pop()
        if curent == finish:
            # return parent
            break
        for i, vertex in enumerate(graph[curent]):
            if vertex == 1 and not is_visited[i]:
                is_visited[i] = True
                parent[i] = curent
                deq.appendleft(i)
    else:
        print('Ooops! No way from start to finish!')
        return [None], -1
    cost = 0
    way = deque([finish])
    i = finish
    while parent[i] != start:
        cost += 1
        way.appendleft(parent[i])
        i = parent[i]
    cost += 1
    way.appendleft(start)
    return list(way), cost


s = int(input())
f = int(input())
print(bfc(graph, s, f))
