# 3. Написать программу, которая обходит не взвешенный ориентированный граф без
# петель, в котором все вершины связаны, по алгоритму поиска в глубину
# (Depth-First Search).
# Примечания:
# a. граф должен храниться в виде списка смежности;
# b. генерация графа выполняется в отдельной функции, которая принимает на вход
# число вершин.
from random import randint


def gen_graph(n):
    """
    :param n: numbers of vertex in unweighted directed graph
    :return: adjacency matrix
    """
    assert n >= 2, 'uncorrect n! n >= 2'
    graph = []
    adj_list = {}
    for i in range(n):
        el = [randint(0, 1) for _ in range(n)]
        while sum(el) < 2:
            el = [randint(0, 1) for _ in range(n)]
        graph.append(el)
    for j in range(n):
        for i in range(n):
            if i == j and graph[i][j] == 1:
                graph[i].insert(j, 0)
                graph[i].pop()
    print(*graph, sep='\n')
    print('*'*50)
    for i in range(len(graph)):
        adj_list[i] = set()
        for idx, vol in enumerate(graph[i]):
            if vol == 1:
                adj_list[i].add(idx)
    return adj_list


num = int(input())
print(gen_graph(num))
