from collections import deque

def bfs(graph, s, t, parent):
    visited = [False] * len(graph)
    queue = deque()
    queue.append(s)
    visited[s] = True

    while queue:
        u = queue.popleft()

        for v in graph.adj[u]:
            if not visited[v] and graph[u][v]['capacity'] - flow[(u, v)] > 0:
                queue.append(v)
                visited[v] = True
                parent[v] = u

    return visited[t]

def edmonds_karp(graph, source, sink):
    parent = [-1] * len(graph)
    max_flow = 0
    global flow
    flow = {}

    for u in graph:
        for v in graph.adj[u]:
            flow[(u, v)] = 0

    while bfs(graph, source, sink, parent):
        path_flow = float("inf")
        s = sink
        while s != source:
            path_flow = min(path_flow, graph[parent[s]][s]['capacity'] - flow[(parent[s], s)])
            s = parent[s]

        max_flow += path_flow

        v = sink
        while v != source:
            u = parent[v]
            flow[(u, v)] += path_flow
            flow[(v, u)] -= path_flow
            v = parent[v]

    return max_flow