import networkx as nx
import random

class Graph:
    def __init__(self):
        self.vertices = {}
        self.copy = {}
    
    def add_edge(self, u, v, capacity):
        if u not in self.vertices:
            self.vertices[u] = {}
            self.copy[u] = {}
        if v not in self.vertices:
            self.vertices[v] = {}
            self.copy[v] = {}
        self.vertices[u][v] = {'capacity': capacity}
        self.copy[u][v] = {'capacity': capacity}
        for v in self.copy:
            for u in self.copy[v]:
                if u not in self.copy or v not in self.copy[u]:
                    self.copy[u][v] = {'capacity': 0}
        for v in self.vertices:
            for u in self.vertices[v]:
                if u not in self.vertices or v not in self.vertices[u]:
                    self.vertices[u][v] = {'capacity': 0}

def read_graph_from_file(filename):
    graph = Graph()
    with open(filename, 'r') as file:
        num_vertices, num_edges = map(int, file.readline().split())
        for _ in range(num_edges):
            u, v, capacity = map(int, file.readline().split())
            graph.add_edge(u, v, capacity)
    return graph

def read_digraph_from_file(filename):
    digraph = nx.DiGraph()
    with open(filename, 'r') as file:
        num_vertices, num_edges = map(int, file.readline().split())
        for _ in range(num_edges):
            u, v, capacity = map(int, file.readline().split())
#             print(u, v, capacity)
            digraph.add_node(u)
            digraph.add_node(v)
            digraph.add_edge(u, v, capacity=capacity)
    return digraph

def generate_graph(vertices, edges, capacity):
    graph = nx.gnm_random_graph(vertices, edges, directed=True)    
    for edge in graph.edges():
        cap = random.randint(1, capacity)
        graph[edge[0]][edge[1]]['capacity'] = cap
    return graph

def convert_to_graph(nx_graph):
    graph = Graph()
    for u in nx_graph.nodes():
        if u not in graph.vertices:
            graph.vertices[u] = {}
        if u not in graph.copy:
            graph.copy[u] = {}

    for u, v, data in nx_graph.edges(data=True):
        capacity = data['capacity']
        graph.add_edge(u, v, capacity)
    
    return graph

# digraph = read_digraph_from_file(filename)

# # Пример использования функции для чтения графа из файла
# filename = "C:\\Users\\Asus\\Downloads\\Cluster_Improvement\\tests\\test_1.txt"  # имя вашего файла
# my_graph = read_graph_from_file(filename)
# # print(my_graph.vertices)
# # print()
# # print(my_graph.copy)