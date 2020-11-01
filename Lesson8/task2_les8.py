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
    :param graph:graph matrix
    :param start:start vertex
    :return:short cut from start to any vertex
    """
    length = len(graph)
    is_visited = []
    # изначально обозначим стоимость пути до любой точки как беcконечность
    costs = {i: float('inf') for i in range(length)}
    parents = {i: None for i in range(length)}
    costs[start] = 0

    # is_visited.append(start)
    def find_low_cost(costs):
        min_cost = float('inf')
        min_cost_node = None
        for node in costs:
            cost = costs[node]
            if cost < min_cost and node not in is_visited:
                min_cost = cost
                min_cost_node = node
        return min_cost_node

    node = find_low_cost(costs)
    way = {i: [0] for i in range(length)}
    while node is not None:
        cost = costs[node]
        neigh = graph[node]
        for n in neigh.keys():
            new_cost = cost + neigh[n]
            if costs[n] > new_cost:
                costs[n] = new_cost
                parents[n] = node
        is_visited.append(node)
        node = find_low_cost(costs)
    way = {i: [] for i in range(length)}
    coopy = parents.copy()
    for key, value in coopy.items():
        if value is None:
            if key == start:
                way[key].append(start)
            else:
                way[key].append(None)
        else:
            way[key].insert(0, key)
            while value != start:
                way[key].insert(0, value)
                value = coopy[value]
            way[key].insert(0, start)


    return f'{parents}\n{costs}\n{way}'

    # cost[start] = 0
    # while min_cost < float('inf'):
    #     is_visited[start] = True
    #     for i, vertex in enumerate(graph[start]):
    #         if vertex != 0 and not is_visited[i]:
    #             if cost[i] > vertex + cost[start]:
    #                 cost[i] = vertex + cost[start]
    #                 parent[i] = start
    #     min_cost = float('inf')
    #     for i in range(length):
    #         if min_cost > cost[i] and not is_visited[i]:
    #             min_cost = cost[i]
    #             start = i
    # return cost


s = int(input('Enter start vertex: '))
graph = adj_lst(graph1)
print(graph)

print(dijkstra(graph, s))
