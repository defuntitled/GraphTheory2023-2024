from graph import Graph, read_graph_from_file, read_digraph_from_file
import networkx as nx
import os, time
from edmonds_karp import edmonds_karp
from fifo_push_relabel import fifo_push_relabel

def main():
    test_directory = "tests"
    for filename in os.listdir(test_directory):
        if filename == 'test_rl10.txt' or filename == 'test_rd07.txt':
            continue
        if filename.endswith(".txt"):
            file_path = os.path.join(test_directory, filename)
            
            my_graph = read_graph_from_file(file_path)
            digraph = read_digraph_from_file(file_path)
            
            source = 1  # источник
            with open(file_path, 'r') as file:
                sink, _ = map(int, file.readline().split()) #сток

            t_fifo = 0
            t_edmonds = 0
            
            expected_result = nx.maximum_flow_value(digraph, source, sink)
            
            start_time = time.perf_counter()
            result_fifo = fifo_push_relabel(my_graph, source, sink)
            finish_time = time.perf_counter()
            if expected_result != result_fifo:
                print(f"mistake {result_fifo} вместо {expected_result}")
            else:
                t_fifo = max(finish_time-start_time, t_fifo)

            start_time = time.perf_counter()
            result_edmonds = edmonds_karp(my_graph, source, sink)
            finish_time = time.perf_counter()
            if expected_result != result_edmonds:
                print(f"mistake {result_edmonds} вместо {expected_result}")
            else:
                t_edmonds = max(finish_time-start_time, t_edmonds)

            print("File:", filename)
            print("FIFO Push Relabel Time:", t_fifo)
            print("Edmonds-Karp Time:", t_edmonds)
            print()
                
main()