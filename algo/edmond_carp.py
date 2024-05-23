import networkx as nx
from pathlib import Path
import random
from networkx.algorithms.flow import preflow_push
from collections import deque
import time

# given
INPUT_PARAMS_PATH = Path("./datasets/input_params.txt")
with INPUT_PARAMS_PATH.open('r') as file:
  params_list = []
  p = file.readline()
  while p:
    params_list.append(tuple(map(int, p.split())))
    p = file.readline()

g = nx.gnm_random_graph(params_list[0][0], params_list[0][1])

# when

def bfs(g, source, sink, parent):
    visited = [False]* len(g.nodes)
    queue = deque([source])
    visited[source] = True

    while queue:
        u = queue.popleft()
        
        for v in g.adj[u]:
            capacity = g[u][v]['capacity']
            if not visited[v] and capacity - g[u][v]['flow'] > 0:
                queue.append(v)
                visited[v] = True
                parent[v] = u

                if v == sink:
                    return True

    return False

# Функция для реализации алгоритма Эдмонда-Карпа
def edmonds_karp(g, source, sink):
    for u in g:
        for v in g.adj[u]:
            g[u][v]['flow'] = 0

    parent = [-1]*len(g.nodes)
    max_flow = 0

    while bfs(g, source, sink, parent):
        path_flow = float('Inf')
        s = sink
        while s != source:
            path_flow = min(path_flow, g[parent[s]][s]['capacity'] - g[parent[s]][s]['flow'])
            s = parent[s]

        v = sink
        while v != source:
            u = parent[v]
            g[u][v]['flow'] += path_flow
            g[v][u]['flow'] -= path_flow  # Обратный поток
            v = parent[v]

        max_flow += path_flow

    return max_flow


# then
t = 0
for i in range(1,len(params_list)):
  for edge in g.edges():
    cap = random.randint(1, params_list[i][2])
    g[edge[0]][edge[1]]['capacity'] = cap
  r = preflow_push(nx.Graph(g), params_list[i][0] -1, params_list[i][1]-1, value_only=True)
  expected_result = r.graph["flow_value"]
  gr = nx.Graph(g)
  start_time=time.perf_counter()
  result = edmonds_karp(gr,params_list[i][0]-1, params_list[i][1]-1)
  finish_time=time.perf_counter()
  t = max(finish_time-start_time,t)
  assert expected_result == result
print(t)