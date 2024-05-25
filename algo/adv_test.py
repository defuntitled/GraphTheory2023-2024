from graph import Graph, generate_graph, convert_to_graph
import networkx as nx
import os, time
import pandas as pd
from edmonds_karp import edmonds_karp
from fifo_push_relabel import fifo_push_relabel

def main():
    
    num_tests_per_graph = 50

    max_capacity = [10, 100, 250, 500, 750, 1000, 2500, 5000, 7500, 10000]
    
    data = []
    for capacity in max_capacity:
        for vertices in range(10, 101, 10):
            for edges_cof in range(10, 101, 10):
                edges = int(vertices * (vertices - 1) // 2 * edges_cof // 100)

                source = 0
                sink = vertices - 1
                
                total_fifo_time = 0
                total_edmonds_time = 0
                
                max_fifo_time = 0
                max_edmonds_time = 0

                for j in range(num_tests_per_graph):
                    nxgraph = generate_graph(vertices, edges, capacity)
                    graph = convert_to_graph(nxgraph)
                    
#                     expected_result = nx.maximum_flow_value(nxgraph, source, sink)


                    start_time = time.perf_counter()
                    result_fifo = fifo_push_relabel(graph, source, sink)
                    finish_time = time.perf_counter()
                    fifo_time = finish_time - start_time
                    total_fifo_time += fifo_time
                    max_fifo_time = max(max_fifo_time,fifo_time)
                    
                    start_time = time.perf_counter()
                    result_edmonds = edmonds_karp(graph, source, sink)
                    finish_time = time.perf_counter()
                    edmonds_time = finish_time - start_time
                    total_edmonds_time += edmonds_time
                    max_edmonds_time = max(max_edmonds_time,edmonds_time)
                    
#                     if expected_result != result_fifo:
#                         print("dismatch")
#                     if expected_result != result_edmonds:
#                         print("dismatch")
                    
                        
                avg_fifo_time = total_fifo_time / num_tests_per_graph
                avg_edmonds_time = total_edmonds_time / num_tests_per_graph

                data.append([vertices, edges, capacity, avg_fifo_time, avg_edmonds_time, max_fifo_time, max_edmonds_time])

    df = pd.DataFrame(data, columns=['vertices', 'edges', 'capacity', 'avg_fifo_time', 'avg_edmonds_time', 'max_fifo_time', 'max_edmonds_time'])
#     print(df)
    df.to_csv("algorithm_runtimes.csv", index=False)

main()