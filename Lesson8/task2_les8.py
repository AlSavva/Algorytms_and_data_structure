# 2. Доработать алгоритм Дейкстры (рассматривался на уроке), чтобы он
# дополнительно возвращал список вершин, которые необходимо обойти.

graph1 = [
    [0, 0, 1, 1, 9, 0, 0, 0],
    [0, 0, 9, 4, 0, 0, 7, 0],
    [0, 9, 0, 0, 3, 0, 6, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 1, 0],
    [0, 0, 0, 0, 0, 0, 5, 0],
    [0, 0, 7, 0, 8, 1, 0, 0],
    [0, 0, 0, 0, 0, 1, 2, 0]
]


def adj_lst(graph):
    """
    Функция трансформирует матрицу смежности графа в лист смежности
    :param graph:adjacency matrix of weighted directed graph
    :return:adjacency list of same graph
    """
    adj_list = {}
    for i in range(len(graph)):
        adj_list[i] = {}
        for idx, vol in enumerate(graph[i]):
            if vol != 0:
                adj_list[i][idx] = vol
    return adj_list


def dijkstra(graph, start):
    """
    Реализация алгоритма Дейкстры, для работы со списком смежности
    :param graph:graph adjacency list
    :param start:start vertex
    # :return:short cut from start to any vertex
    """
    length = len(graph)
    is_visited = []
    costs = {i: float('inf') for i in range(length)}
    parents = {i: None for i in range(length)}
    costs[start] = 0

    def find_min_cost(costs):
        """
        Функция ищет вершину с наименьшей стоимостью достижения
        """
        min_cost = float('inf')
        min_cost_vertex = None
        for vertex in costs:
            cost = costs[vertex]
            if cost < min_cost and vertex not in is_visited:
                min_cost = cost
                min_cost_vertex = vertex
        return min_cost_vertex

    vertex = find_min_cost(costs)
    while vertex is not None:
        cost = costs[vertex]
        neighbor = graph[vertex]
        for n in neighbor.keys():
            new_cost = cost + neighbor[n]
            if costs[n] > new_cost:
                costs[n] = new_cost
                parents[n] = vertex
        is_visited.append(vertex)
        vertex = find_min_cost(costs)
    # доработка, для вывода самого дешегого пути для любой вершины при обходе
    # графа
    way = {i: [] for i in range(length)}
    for key, value in parents.items():
        if value is None:
            if key == start:
                way[key].append(start)
            else:
                way[key].append(None)
        else:
            way[key].insert(0, key)
            while value != start:
                way[key].insert(0, value)
                value = parents[value]
            way[key].insert(0, start)

    # return costs # возвращает стоимость достижения любой вешины из точки start
    return way  # Возвращает самый дешевый маршрут до любой вершины из точки start



s = int(input('Enter start vertex: '))
graph = adj_lst(graph1)
print(graph)

print(dijkstra(graph, s))
