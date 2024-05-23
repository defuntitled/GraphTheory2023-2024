from collections import deque

def initialize_preflow(graph, s):
    n = graph.number_of_nodes()
    height = [0]*n
    excess = [0]*n
    flow = {}

    height[s] = n
    for u in graph:
        for v in graph.adj[u]:
            flow[(u, v)] = 0

    for v in graph.adj[s]:
        flow[(s, v)] = graph[s][v]['capacity']
        flow[(v, s)] = -flow[(s, v)]
        excess[v] = flow[(s, v)]
        excess[s] -= flow[(s, v)]

    return height, excess, flow

def push(u, v, excess, flow, graph):
    delta = min(excess[u], graph[u][v]['capacity'] - flow[(u, v)])
    flow[(u, v)] += delta
    flow[(v, u)] -= delta
    excess[u] -= delta
    excess[v] += delta

def relabel(u, height, graph, flow):
    min_height = float('inf')
    for v in graph.adj[u]:
        if graph[u][v]['capacity'] - flow[(u, v)] > 0:
            min_height = min(min_height, height[v])
    height[u] = min_height + 1

def discharge(u, height, excess, flow, graph, queue,in_queue,s,t):
    while excess[u] > 0:
        for v in graph.adj[u]:
            if graph[u][v]['capacity'] - flow[(u, v)] > 0 and height[u] == height[v] + 1:
                push(u, v, excess, flow, graph)
                if not in_queue[v] and v != s and v != t:
                    queue.append(v)
                    in_queue[v] = True
        relabel(u, height, graph, flow)

def fifo_push_relabel_impl(graph, s, t):
    height, excess, flow = initialize_preflow(graph, s)
    queue = deque([u for u in graph.adj[s] if u != s and u != t and excess[u] > 0])
    in_queue = [v in queue for v in graph.nodes]

    while queue:
        u = queue.popleft()
        in_queue[u] = False
        discharge(u, height, excess, flow, graph, queue,in_queue, s, t)
        if excess[u] > 0:
            queue.append(u)
            in_queue[u] = True

    max_flow = sum(flow[(s, v)] for v in graph.adj[s])
    return max_flow