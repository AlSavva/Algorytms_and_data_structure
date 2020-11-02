import random


def graph_gen(vertex):
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


def dfs(graph, start, waydct=None, is_vis=None):
    if waydct is None:
        waydct = {}
    if is_vis is None:
        is_vis = set()
    waydct[start] = list(graph[start])
    is_vis.add(start)
    print(waydct, is_vis)
    for i in range(len(waydct[start])):
        if waydct[start][i] not in is_vis:
            waydct[start][i] = dfs(graph, waydct[start][i], waydct[start])
        return waydct

#
# from collections import defaultdict
# def dfs(graph,v,seen=None,path=None):
#     if seen is None:
#         seen = []
#     if path is None:
#         path = [v]
#         seen.append(v)
#     paths = []
#     for t in graph[v]:
#         if t not in seen:
#             t_path = path + [t]
#             paths.append(tuple(t_path))
#             paths.extend(dfs(graph, t, seen[:], t_path))
#         return paths # Define graph by edges edges = [['1', '2'], ['2', '4'], ['1', '11'], ['4', '11']] # Build graph dictionary G = defaultdict(list) for (s,t) in edges: G[s].append(t) G[t].append(s) # Run DFS, compute metrics all_paths = DFS(G, '1') max_len = max(len(p) for p in all_paths) max_paths = [p for p in all_paths if len(p) == max_len] # Output print("All Paths:") print(all_paths) print("Longest Paths:") for p in max_paths: print(" ", p) print("Longest Path Length:") print(max_len)

graph = graph_gen(5)
print(graph)
print(dfs(graph,0))
