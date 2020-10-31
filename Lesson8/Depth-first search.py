# Алгоритм поиска (или обхода) в глубину (англ. depth-first search, DFS)
# позволяет построить обход ориентированного или неориентированного графа,
# при котором посещаются все вершины, доступные из начальной вершины.
# Результатом работы алгоритма является некоторый маршрут, следуя
# которому можно обойти последовательно все вершины графа, доступные из
# начальной вершины.
# В каждый момент исполнения алгоритма обрабатывается только одна
# вершина.
# DFS не находит кратчайших путей, но он применим в ситуациях, когда граф
# неизвестен целиком, а исследуется каким-то автоматизированным
# устройством.
# Для ориентированного графа DFS строит дерево путей из начальной
# вершины во все доступные из нее.

# Алгоритм поиска в глубину
# 1 Пойти в какую-нибудь смежную вершину, не посещенную ранее.
# 2 Запустить из этой вершины алгоритм обхода в глубину
# 3 Вернуться в начальную вершину.
# 4 Повторить пункты 1-3 для всех не посещенных ранее смежных вершин.

graph = {
    0: {1, 4},
    1: {2, 3, 4},
    2: {0, 1, 3, 4},
    3: {1, 2},
    4: {1, 2}
}

def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()
    visited.add(start)
    print(start)
    for next in graph[start] - visited:
        dfs(graph, next, visited)
    return visited
    # visited = set()
    # rout = []
    # visited.add(start)
    # for i in range(len(graph)):
    #     if graph[start][i] == 1 and i not in visited:
    #         print(i)
    #         dfs(i)
    #     return rout

dfs(graph, 0)
