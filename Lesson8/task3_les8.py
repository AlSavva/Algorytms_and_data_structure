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
    return graph


num = int(input())
print(*gen_graph(num), sep='\n')
