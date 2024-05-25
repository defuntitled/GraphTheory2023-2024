from graph import Graph

def fifo_push_relabel(graph, source, sink):
    queue = []
    excess = {u: 0 for u in graph.vertices}
    height = {u: 0 for u in graph.vertices}
    inQueue = {u: False for u in graph.vertices}
    height[source] = len(graph.vertices)
    
    graph_residual  = graph.copy
    
    for v in graph_residual[source]:
        if graph_residual[source][v]['capacity'] != 0:
            graph_residual[source][v]['capacity'] = 0
            graph_residual[v][source]['capacity'] = graph.vertices[source][v]['capacity']
            excess[v] = graph_residual[v][source]['capacity']
            if v != sink:
                queue.append(v)
                inQueue[v] = True
    
    while queue:
        u = queue.pop(0)
        inQueue[u] = False
        relabel(graph_residual, u, height)
        push(graph_residual, u, excess, height, queue, inQueue, source, sink)
    
    return excess[sink]

def relabel(graph, u, height):
    minHeight = float("inf")
    for v in graph[u]:
        if graph[u][v]['capacity'] > 0:
            minHeight = min(minHeight, height[v])
            height[u] = minHeight + 1

def push(graph, u, excess, height, queue, in_queue, source, sink):
    for v in graph[u]:
        if excess[u] == 0:
            break

        if graph[u][v]['capacity'] > 0 and height[v] < height[u]:
            flow = min(excess[u], graph[u][v]['capacity'])

            graph[u][v]['capacity'] -= flow
            graph[v][u]['capacity'] += flow

            excess[u] -= flow
            excess[v] += flow

            if not in_queue[v] and v != source and v != sink:
                queue.append(v)
                in_queue[v] = True

    if excess[u] != 0:
        queue.append(u)
        in_queue[u] = True


# source = 1  # источник
# with open(filename, 'r') as file:
#     sink, _ = map(int, file.readline().split())
# max_flow = fifo_push_relabel(my_graph, source, sink)
# print("Максимальный поток:", max_flow)