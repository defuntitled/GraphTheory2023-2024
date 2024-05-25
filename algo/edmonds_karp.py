from collections import deque
from graph import Graph

def find_augmenting_path(graph, source, sink, parent):
    visited = {u: False for u in graph.vertices}
    queue = deque()
    queue.append(source)
    visited[source] = True

    while queue:
        u = queue.popleft()
        for v in graph.vertices[u]:
            if not visited[v] and graph.vertices[u][v]['capacity'] > 0:
                queue.append(v)
                visited[v] = True
                parent[v] = u
                if v == sink:
                    return True
    return False

def edmonds_karp(graph, source, sink):
    max_flow = 0
    parent = {u: None for u in graph.vertices}

    while find_augmenting_path(graph, source, sink, parent):
        # Находим минимальную пропускную способность на пути
        path_flow = float("inf")
        v = sink
        while v != source:
            u = parent[v]
            path_flow = min(path_flow, graph.vertices[u][v]['capacity'])
            v = parent[v]

        # Обновляем пропускные способности на пути и обратных рёбрах
        v = sink
        while v != source:
            u = parent[v]
            graph.vertices[u][v]['capacity'] -= path_flow
            # Убедимся, что обратное ребро существует в графе
            if u in graph.vertices[v]:
                graph.vertices[v][u]['capacity'] += path_flow
            else:
                # Если обратного ребра нет, добавим его с пропускной способностью path_flow
                graph.add_edge(v, u, path_flow)
            v = parent[v]

        max_flow += path_flow

    return max_flow


# # Пример использования функции для чтения графа из файла
# filename = "C:\\Users\\Asus\\Downloads\\Cluster_Improvement\\tests\\test_1.txt"  # имя вашего файла
# my_graph = read_graph_from_file(filename)
# # print(my_graph.vertices)
# source = 1  # источник
# with open(filename, 'r') as file:
#     sink, _ = map(int, file.readline().split())
# max_flow = edmonds_karp(my_graph, source, sink)
# print("Максимальный поток:", max_flow)
