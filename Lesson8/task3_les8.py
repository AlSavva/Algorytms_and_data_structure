# 3. Написать программу, которая обходит не взвешенный ориентированный граф без
# петель, в котором все вершины связаны, по алгоритму поиска в глубину
# (Depth-First Search).
# Примечания:
# a. граф должен храниться в виде списка смежности;
# b. генерация графа выполняется в отдельной функции, которая принимает на вход
# число вершин.
import random


def gen_graph(vertex):
    """
    Функция генерирует направленный связанный граф без петель в виде списка
    смежности
    :param vertex: number of vertex
    :return:adjacency list
    """
    graph = {}
    for i in range(vertex):
        edges = []
        while len(
                edges) < 2:  # обеспечиваем минимум 2 ребра при каждой вершине
            edges = random.choices(list(range(vertex)),
                                   k=random.randint(2, vertex - 1))
            edges = set(edges)
            edges.discard(i)  # обеспечиваем отсутствие петель
        graph[i] = edges
    return graph

vislst = []
def dfs(graph, start, visited=None, count=1):
    global  dct
    dct={}

    if visited is None:
        visited = set()
    visited.add(start)
    dct[start] = visited
    print(start)
    if not graph[start] - visited:
        print('************')
    for next in graph[start] - visited:
        dfs(graph, next, visited, count=1)
    return dct


num = int(input())
graph = gen_graph(num)
print(graph)
print(dfs(graph, 0))
