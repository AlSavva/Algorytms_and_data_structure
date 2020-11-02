# 3. Написать программу, которая обходит не взвешенный ориентированный граф без
# петель, в котором все вершины связаны, по алгоритму поиска в глубину
# (Depth-First Search).
# Примечания:
# a. граф должен храниться в виде списка смежности;
# b. генерация графа выполняется в отдельной функции, которая принимает на вход
# число вершин.
import random


def gen_graph(vertex, percent=1.0):
    """
    Функция принимает на вход 2 значения - количество вершин в графе и процент
    который будет регулировать максимальное количество реберб исходящих от
    вершины.
    """
    assert 0 < percent <= 1, 'uncorrect value! 0 < percent <= 1!'
    graph = {}
    for i in range(vertex):
        graph[i] = set()
        count_edge = random.randrange(1, int(vertex * percent))
        while len(graph[i]) < count_edge:
            edge = random.randrange(0, vertex)
            if edge != i:
                graph[i].add(edge)
    return graph


def dfs(graph, start):
    path = []  # храним путь, по которому движемся
    parent = [None for _ in range(len(graph))]
    is_visited = [False for _ in range(len(graph))]

    def _dfs(vertex):
        """
        обходит граф и вызывает сама себя
        """
        is_visited[vertex] = True  # отмечаем вершину посещённой
        path.append(vertex)  # добавляем вершину к пути
        for item in graph[vertex]:
            if not is_visited[
                item]:  # если очередная вершина еще не была посещена
                parent[item] = vertex  # добавляем в список ее родителей
                _dfs(item)  # рекурсивно вызываем со значением новой вершины
                path.append(vertex)  # добавляем в путь вершину
        else:  # если из вершины нет пути в непосещенные вершины - делаем шаг назад.
            path.append(-vertex)

    _dfs(start)
    return parent, path


g = gen_graph(int(input('Enter numbers of vertex: ')),
              float(input('Enter percent of edge: ')))
print(g)
for key, value in g.items():
    print(f'From vertex "{key}" edges lead to vertex {value}')
s = int(input('Enter start-vertex: '))
parent, path = dfs(g, s)
print(parent)
for i, vertex in enumerate(path):
    if i % 10 == 0: # оформление вывода - по 10 значений
        print()
    print(f'{vertex:>4};', end='')